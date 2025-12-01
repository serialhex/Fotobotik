from google.adk.tools import ToolContext
import google.genai.types as types
import face_recognition
import logging
import numpy as np
from PIL import Image
from io import BytesIO

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
                "tool_response_artifact_id": image_artifact,
                "tool_input_artifact_ids": "",
                "message": f"Artifact {image_id} not found."
            }

        # This is where we begin the actual work
        image_data = image_artifact.inline_data.data
        artifact_id = f"{image_id}_faces"
        people = _extract_faces(image_data)
        for img, name in people:
            # Come up with a better naming scheme...
            await tool_context.save_artifact(filename=f"{name}.png",
                artifact=_pack_artifact(img))

        return {
            "status": "success",
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

def _pack_artifact(image_bytes):
    return types.Part(
        inline_data=types.Blob(data=image_bytes, mime_type="image/png")
    )

def _load_part_data(artifact):
    data = image_artifact.inline_data.data
    return _bin_img_to_np(data)

def _bin_img_to_np(data):
    img = Image.open(BytesIO(data))
    return np.array(img)

def _box_faces(image):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    pil_image = Image.fromarray(image)
    draw = ImageDraw(pil_image)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))

def _extract_faces(image_data):
    image = _bin_img_to_np(image_data)

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    pil_image = Image.fromarray(image)

    face = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        box = (left, top, right, bottom)
        face.append(pil_image.crop(box))

    # Write an actual implementation to detect faces here...
    people = ["Jane", "Kenji", "Miki", "Gomer", "Lala"]
    return list(zip(face, people))
