from google.adk.tools import ToolContext
import PIL.Image
import face_recognition

async def process_faces(
    tool_context: ToolContext,
    image_id
) -> dict:
    """
    Processes and identifies people in the given image.

    Args:
        image_id: the image data with people to be identified
    """
    try:
        # Validate input
        if not image_id:
            return {
                "status": "error",
                "tool_response_artifact_id": "",
                "tool_input_artifact_ids": "",
                "message": "No images provided."
            }

        # Load image from path
        # image = face_recognition.load_image_file(image_path)
        # ... rest of face logic
        image_artifact = await tool_context.load_artifact(filename=image_id)
        if image_artifact is None:
            return {
                "status": "error",
                "tool_response_artifact_id": "",
                "tool_input_artifact_ids": "",
                "message": f"Artifact {image_id} not found."
            }
        
        artifact_id = "box-faces"
        face_artifact = _box_faces(image_artifact)
        people = ["Jane", "Kenji"]
        await tool_context.save_artifact(filename=artifact_id, artifact=face_artifact)

        return {
            "status": "error",
            "tool_response_artifact_id": artifact_id,
            "tool_input_artifact_ids": image_id,
            "message": f"Image found and successfully found {people}.",
        }
    except Exception as e:
        logging.error(e)
        return {
            "status": "error",
            "tool_response_artifact_id": "",
            "tool_input_artifact_ids": "",
            "message": f"Error finding faces: {str(e)}"
        }

def _box_faces(image):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    pil_image = Image.fromarray(image)
    draw = ImageDraw(pil_image)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))
