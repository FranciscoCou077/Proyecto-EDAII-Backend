from fastapi import APIRouter, UploadFile, File, HTTPException
from app.algoritmos.archivos.operaciones import save_uploaded_file, get_file_info

router = APIRouter()


@router.post("/create")
async def create_file(file: UploadFile = File(...)):
    saved_path = save_uploaded_file(file)
    return {"message": "Archivo guardado", "filename": file.filename, "path": saved_path}


@router.get("/info")
def get_info(filename: str):
    try:
        info = get_file_info(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return info
