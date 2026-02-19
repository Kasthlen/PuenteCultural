from crewai import Crew, Process
from app.agents.agents import PuenteCulturalAgents
from app.agents.tasks import PuenteCulturalTasks
from app.agents.free_engine import FreeContentGenerator
import os

class GeneradorContenidoCrew:
    def __init__(self, tema, materia, perfil_alumnos):
        self.tema = tema
        self.materia = materia
        self.perfil_alumnos = perfil_alumnos
        self.agents = PuenteCulturalAgents()
        self.tasks = PuenteCulturalTasks()
        self.free_engine = FreeContentGenerator()
        self.llm_mode = self._clean_env(os.getenv("LLM_MODE", "api")).lower()
        self.fallback_mode = self._clean_env(os.getenv("FALLBACK_MODE", "raise")).lower()

    @staticmethod
    def _clean_env(value: str):
        return value.strip().strip('"').strip("'").rstrip(",").strip()

    def run(self):
        if self.llm_mode == "rules":
            return self.free_engine.generate(self.tema, self.materia, self.perfil_alumnos)

        # 1. Seleccionar el agente especialista según la materia
        if self.materia.lower() == "historia":
            especialista = self.agents.agente_historia()
            # Pasamos el agente al método de la tarea para que se asigne correctamente
            tarea_analisis = self.tasks.analisis_historia_task(especialista, self.tema, self.perfil_alumnos)
            
        elif self.materia.lower() == "literatura":
            especialista = self.agents.agente_literatura()
            tarea_analisis = self.tasks.analisis_literatura_task(especialista, self.tema, self.perfil_alumnos)
            
        elif self.materia.lower() == "ingles":
            especialista = self.agents.agente_ingles()
            tarea_analisis = self.tasks.analisis_ingles_task(especialista, self.tema, self.perfil_alumnos)
            
        else:
            return f"Error: La materia '{self.materia}' no está soportada actualmente."

        # 2. El coordinador siempre está presente para empaquetar el resultado final
        coordinador = self.agents.coordinador_pedagogico()
        tarea_sintesis = self.tasks.sintesis_guia_docente_task(coordinador, self.tema, self.materia)

        # 3. Crear la "Tripulación" (Crew)
        # IMPORTANTE: memory=False evita que CrewAI intente usar OpenAI para embeddings
        crew = Crew(
            agents=[especialista, coordinador],
            tasks=[tarea_analisis, tarea_sintesis],
            process=Process.sequential,  # Ejecución secuencial: primero analiza, luego sintetiza
            verbose=True,
            memory=False,   # <--- ESTA ES LA CLAVE DEL ÉXITO
            embedder=None   # Aseguramos que no busque vector store
        )

        # 4. ¡Acción!
        try:
            result = crew.kickoff()
            return result
        except Exception as error:
            error_texto = str(error).lower()
            if self.fallback_mode == "rules" and any(
                clave in error_texto for clave in ["429", "quota", "model_not_found", "resource_exhausted", "api key"]
            ):
                return self.free_engine.generate(self.tema, self.materia, self.perfil_alumnos)
            raise