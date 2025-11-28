import face_recognition
from PIL import Image, ImageDraw
import numpy as np

def _box_faces(image):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))
    
    del draw
    pil_image.show()

if __name__ == "__main__":
    img = face_recognition.load_image_file("test-imgs/1763841048.png")
    _box_faces(img)
