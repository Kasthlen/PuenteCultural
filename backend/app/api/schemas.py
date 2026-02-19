from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    tema: str = Field(..., min_length=3, max_length=200)
    materia: str = Field(..., min_length=3, max_length=80)
    perfil_alumnos: str = Field(..., min_length=5, max_length=400)


class GenerateResponse(BaseModel):
    resultado: str
