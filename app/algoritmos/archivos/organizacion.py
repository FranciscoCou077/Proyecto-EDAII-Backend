import os

UPLOAD_DIR = "uploads"


def ensure_upload_dir():
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    return UPLOAD_DIR


def get_upload_path(filename: str) -> str:
    return os.path.join(ensure_upload_dir(), filename)
