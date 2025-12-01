import face_recognition
from PIL import Image, ImageDraw
import numpy as np
from io import BytesIO

def _box_faces(image_data):
    image = _bin_img_to_np(image_data)

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))

    del draw
    pil_image.show()

def _extract_faces(image_data):
    image = _bin_img_to_np(image_data)

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    pil_image = Image.fromarray(image)

    arr = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        box = (left, top, right, bottom)
        arr.append(pil_image.crop(box))

    # Write an actual implementation to detect faces here...
    people = ["Jane", "Kenji"]
    return (arr, people)

def _load_image_as_binary(image_path):
    b = open(image_path, 'rb').read()
    return b

def _bin_img_to_np(data):
    img = Image.open(BytesIO(data))
    return np.array(img)

if __name__ == "__main__":
    b = _load_image_as_binary("test-imgs/1763841536.png")
    # _box_faces(b)

    (imgs, ppl) = _extract_faces(b)
    for img in imgs:
        img.show()
