from crewai import Agent, LLM
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class PuenteCulturalAgents:
    def __init__(self):
        llm_mode = self._clean_env(os.getenv("LLM_MODE", "api")).lower()
        if llm_mode == "rules":
            self.llm = None
            return

        # Configurar modelo principal y fallback
        primary_model = self._clean_env(os.getenv("MODEL", "github/gpt-4o-mini"))
        fallback_model = self._clean_env(os.getenv("FALLBACK_MODEL", "gemini/gemini-2.0-flash"))
        temperature = float(self._clean_env(os.getenv("TEMPERATURE", "0.5")))

        # Intentar con modelo principal primero
        api_key, base_url = self._resolve_llm_config(primary_model)
        if api_key:
            try:
                llm_params = {
                    "model": primary_model,
                    "temperature": temperature,
                    "api_key": api_key,
                }
                if base_url:
                    llm_params["base_url"] = base_url
                self.llm = LLM(**llm_params)
                return
            except Exception as e:
                print(f"Error con modelo principal {primary_model}: {e}")

        # Fallback al modelo secundario
        api_key, base_url = self._resolve_llm_config(fallback_model)
        if not api_key:
            raise ValueError(
                "No se encontró API key para ejecutar LLM real. "
                "Configura LLM_API_KEY o la key del proveedor (GitHub Models/Gemini)."
            )

        llm_params = {
            "model": fallback_model,
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

        if model_lower.startswith("gemini/"):
            api_key = (
                PuenteCulturalAgents._clean_env(os.getenv("GeminiPuenteCultural"))
                or PuenteCulturalAgents._clean_env(os.getenv("GEMINI_API_KEY"))
                or PuenteCulturalAgents._clean_env(os.getenv("GOOGLE_API_KEY"))
            )
            return api_key or None, explicit_base_url or None

        if model_lower.startswith("anthropic/") or model_lower.startswith("claude"):
            api_key = PuenteCulturalAgents._clean_env(os.getenv("ANTHROPIC_API_KEY"))
            return api_key or None, explicit_base_url or None

        if model_lower.startswith("github/"):
            api_key = (
                PuenteCulturalAgents._clean_env(os.getenv("GithubPuenteCultural"))
                or PuenteCulturalAgents._clean_env(os.getenv("GITHUB_API_KEY"))
                or PuenteCulturalAgents._clean_env(os.getenv("GITHUB_TOKEN"))
                or PuenteCulturalAgents._clean_env(os.getenv("GH_TOKEN"))
            )
            base_url = explicit_base_url or "https://models.inference.ai.azure.com"
            return api_key or None, base_url

        # Solo soportamos GitHub Models y Gemini, no OpenAI
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