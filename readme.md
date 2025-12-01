# Fotobotik

An agent & application designed to aid in organizing photos and reliving memories.
This tool is meant to assist in organizing messy photo libraries, eventually using local tools for everything!


## How to run for the first time

```sh
sudo pacman -S uv
uv venv
uv pip install face_recognition google-adk exifread pillow pillow-heif face_recognition_models distribute setuptools
# The following simply tests that `face_recognition` works, not necessary
uv run test_recognition.py
uv run adk web
```
