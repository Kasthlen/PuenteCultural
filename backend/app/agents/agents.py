from crewai import Agent, LLM
import os
from dotenv import load_dotenv

# Cargar variables de entorno (solo si existe archivo .env, usar env vars del sistema)
load_dotenv(override=False)

class PuenteCulturalAgents:
    def __init__(self):
        llm_mode = self._clean_env(os.getenv("LLM_MODE", "api")).lower()
        if llm_mode == "rules":
            self.llm = None
            return

        # Solo GitHub Models como proveedor
        model_name = self._clean_env(os.getenv("MODEL", "github/gpt-4o-mini"))
        temperature = float(self._clean_env(os.getenv("TEMPERATURE", "0.5")))

        # Debug: imprimir variables disponibles
        print(f"DEBUG: LLM_MODE={llm_mode}")
        print(f"DEBUG: MODEL={model_name}")
        print(f"DEBUG: GithubPuenteCultural exists: {bool(os.getenv('GithubPuenteCultural'))}")
        print(f"DEBUG: GITHUB_API_KEY exists: {bool(os.getenv('GITHUB_API_KEY'))}")
        print(f"DEBUG: GITHUB_TOKEN exists: {bool(os.getenv('GITHUB_TOKEN'))}")
        print(f"DEBUG: GH_TOKEN exists: {bool(os.getenv('GH_TOKEN'))}")

        api_key, base_url = self._resolve_llm_config(model_name)
        if not api_key:
            print(f"DEBUG: No API key found. Available env vars: {[k for k in os.environ.keys() if 'GITHUB' in k or 'Github' in k]}")
            raise ValueError(
                "No se encontró API key para ejecutar LLM real. "
                "Configura GithubPuenteCultural o GITHUB_API_KEY para GitHub Models."
            )

        llm_params = {
            "model": model_name,
            "temperature": temperature,
            "api_key": api_key,
        }
        if base_url:
            llm_params["base_url"] = base_url

        self.llm = LLM(**llm_params)

    @staticmethod
    def _clean_env(value: str | None):
        if value is None:
            return ""
        return value.strip().strip('"').strip("'").rstrip(",").strip()

    @staticmethod
    def _resolve_llm_config(model_name: str):
        explicit_api_key = PuenteCulturalAgents._clean_env(os.getenv("LLM_API_KEY"))
        explicit_base_url = PuenteCulturalAgents._clean_env(os.getenv("LLM_BASE_URL"))
        if explicit_api_key:
            return explicit_api_key, explicit_base_url or None

        model_lower = model_name.lower()

        # Solo soportamos GitHub Models
        if model_lower.startswith("github/"):
            api_key = (
                PuenteCulturalAgents._clean_env(os.getenv("GithubPuenteCultural"))
                or PuenteCulturalAgents._clean_env(os.getenv("GITHUB_API_KEY"))
                or PuenteCulturalAgents._clean_env(os.getenv("GITHUB_TOKEN"))
                or PuenteCulturalAgents._clean_env(os.getenv("GH_TOKEN"))
            )
            base_url = explicit_base_url or "https://models.inference.ai.azure.com"
            return api_key or None, base_url

        # No soportamos otros proveedores
        return None, None

    def agente_historia(self):
        return Agent(
            role='Historiador Mediador Cultural',
            goal='Adaptar lecciones de Historia de España para estudiantes latinoamericanos.',
            backstory="Eres un catedrático de Historia experto en relaciones España-América Latina.",
            allow_delegation=False,
            verbose=True,
            max_retry_limit=1,
            llm=self.llm
        )

    def agente_literatura(self):
        return Agent(
            role='Experto en Literatura Comparada',
            goal='Hacer accesibles los textos clásicos españoles.',
            backstory="Eres un filólogo especializado en enseñar a extranjeros.",
            allow_delegation=False,
            verbose=True,
            max_retry_limit=1,
            llm=self.llm
        )

    def agente_ingles(self):
        return Agent(
            role='Lingüista de Inglés',
            goal='Enseñar inglés anticipándose a los errores de hispanohablantes.',
            backstory="Eres un profesor experto en False Friends.",
            allow_delegation=False,
            verbose=True,
            max_retry_limit=1,
            llm=self.llm
        )

    def coordinador_pedagogico(self):
        return Agent(
            role='Diseñador Instruccional',
            goal='Sintetizar la información en una Guía Docente clara.',
            backstory="Eres un experto en pedagogía que estructura fichas de clase.",
            allow_delegation=True,
            verbose=True,
            max_retry_limit=1,
            llm=self.llm
        )