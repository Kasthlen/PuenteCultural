from fastapi import APIRouter, HTTPException

from app.agents.crew import GeneradorContenidoCrew
from app.api.schemas import GenerateRequest, GenerateResponse


router = APIRouter(tags=["generacion"])


@router.post("/generate", response_model=GenerateResponse)
def generate_docente(payload: GenerateRequest) -> GenerateResponse:
    try:
        generador = GeneradorContenidoCrew(
            tema=payload.tema,
            materia=payload.materia,
            perfil_alumnos=payload.perfil_alumnos,
        )
        resultado = generador.run()
        return GenerateResponse(resultado=str(resultado))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error interno generando contenido: {error}") from error
