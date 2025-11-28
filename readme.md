# Fotobotik


## How to run for the first time

```sh
sudo pacman -S uv
uv venv
uv pip install face_recognition google-adk exifread pillow pillow-heif face_recognition_models distribute setuptools
# The following tests that `face_recognition` works
uv run test_recognition.py
uv run adk web
```
