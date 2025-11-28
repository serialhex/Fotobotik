from google.adk.tools.agent_tool import AgentTool
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google.genai import types
from base64 import b64decode, b64encode

from fotobotik.face_processing import process_faces
from fotobotik.model_callbacks import before_model_modifier

#####################################################################

retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

image_describer = Agent(
    name="image_describer",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="An agent that describes images and outputs it into a specified JSON object.",
    instruction="""
Analyze this image and describe it in structured JSON format.

Respond with a JSON object containing these keys:

{
  "scene_summary": "One sentence describing the overall scene, setting, time of day, and mood. Do not list people or objects.",
  "environment": "Either 'indoor' or 'outdoor'",
  "location_type": "Type of place (e.g. 'kitchen', 'beach', 'office', 'forest', 'park', 'bedroom')",
  "objects": ["List", "of", "notable", "non-person", "objects", "visible"],
  "activities": ["List", "of", "what", "people", "are", "doing"],
  "lighting": "Brief description of lighting (e.g. 'sunny', 'overcast', 'golden hour', 'fluorescent', 'dim indoor')",
  "event_type": "Type of event, if any (e.g. 'birthday', 'wedding', 'holiday', 'graduation', null if none)",
  "people": [
    {
      "description": "physical description and clothing",
      "known": false,
      "identity": "",
      "confidence": "low|medium|high"
    },
    {
      "description": "green sweater, blue jeans, long hair",
      "known": true,
      "identity": "jane",
      "confidence": "high"
    }
  ]
}

Rules:
- For 'people', describe each visible person with their clothing and appearance
- Set 'known' to true only if you can identify the person by name
- If 'known' is true, put the name in 'identity'; if false, use empty string
- Set 'confidence' based on how sure you are about the description
- Use lowercase for all string values unless it's a proper noun.
- If uncertain about a category, return null or an empty list.
- Respond with ONLY the JSON object. No other text.
"""
)

image_agent = Agent(
    name="image_describer",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="An agent that describes images and outputs it into a specified JSON object.",
    instruction="""
**IMPORTANT: Base64 Argument Rule on Tool Call**

If you found any tool call arguments that requires base64 data,
ALWAYS provide the artifact_id of the referenced file to 
the tool call. NEVER ask user to provide base64 data. 
Base64 data encoding process is out of your 
responsibility and will be handled in another part of the system.
""",
    tools=[AgentTool(agent=image_describer), process_faces],
)

root_agent = Agent(
    name="fotobotik",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="The base Fotobotik Agent.",
    instruction="""
You are Fotobotik, a helpful photo organizing agent. Your role is to assist users in organizing their photo collections by analyzing images, extracting metadata, identifying faces, and describing content to create structured, searchable photo libraries.

Work through the photo organization process step-by-step using available tools. Extract EXIF data, identify known faces, describe image content with multimodal vision, and organize photos into appropriate folders based on date or events. Compile all gathered information into a searchable index.

Maintain a helpful, friendly tone while being efficient and thorough in your photo management tasks.
""",
    tools=[
        # AgentTool(agent=image_agent)
        process_faces
    ],
    before_model_callback=before_model_modifier
)

runner = InMemoryRunner(agent=root_agent)
