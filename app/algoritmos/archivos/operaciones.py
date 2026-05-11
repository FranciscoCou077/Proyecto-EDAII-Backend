import os
from typing import Dict
from fastapi import UploadFile
from .organizacion import get_upload_path


def save_uploaded_file(file: UploadFile) -> str:
    file_path = get_upload_path(file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path


def get_file_info(filename: str) -> Dict[str, object]:
    file_path = get_upload_path(filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Archivo no encontrado: {filename}")
    stats = os.stat(file_path)
    return {
        "nombre": filename,
        "tamaño_bytes": stats.st_size,
        "creacion": stats.st_ctime,
    }
