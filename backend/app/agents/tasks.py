from crewai import Task
from textwrap import dedent

class PuenteCulturalTasks:
    """
    Definición de las tareas que realizarán los agentes.
    Cada tarea tiene una descripción clara y un formato de salida esperado.
    """

    def analisis_historia_task(self, agent, tema, perfil_alumnos):
        return Task(
            description=dedent(f"""
                Analiza el siguiente tema del currículo de Historia de España: '{tema}'.
                El aula tiene estudiantes con el siguiente perfil: {perfil_alumnos}.

                Tu tarea es:
                1. Identificar los conceptos clave del tema que pueden ser ajenos culturalmente.
                2. Buscar analogías históricas específicas con los países de origen de los alumnos.
                3. Detectar posible vocabulario histórico conflictivo o desconocido.
            """),
            expected_output=dedent("""
                Un informe de análisis cultural que incluya:
                - Conceptos Clave Explicados.
                - Tabla de Analogías (Hecho España vs Hecho País Origen).
                - Lista de términos históricos a aclarar.
            """),
            agent=agent
        )

    def analisis_literatura_task(self, agent, tema, perfil_alumnos):
        return Task(
            description=dedent(f"""
                Analiza el tema o obra literaria: '{tema}'.
                Perfil de estudiantes: {perfil_alumnos}.

                Tu tarea es:
                1. Identificar barreras lingüísticas (español arcaico vs español moderno/latino).
                2. Encontrar temas universales en la obra que conecten con la cultura de los alumnos.
                3. Sugerir una breve explicación contextual para antes de la lectura.
            """),
            expected_output=dedent("""
                Una guía de lectura inclusiva que contenga:
                - Glosario de 'Traducción Cultural' (Español Antiguo -> Español Latam actual).
                - Conexiones temáticas universales.
                - Gancho introductorio para motivar la lectura.
            """),
            agent=agent
        )

    def analisis_ingles_task(self, agent, tema, perfil_alumnos):
        return Task(
            description=dedent(f"""
                Prepara una lección sobre el tema de gramática/vocabulario: '{tema}'.
                Perfil de estudiantes: {perfil_alumnos} (Hispanohablantes de diversas regiones).

                Tu tarea es:
                1. Predecir los errores de 'False Friends' o interferencia de L1 (Español) específicos para este tema.
                2. Si el tema tiene diferencias marcadas entre Inglés Británico (enseñado en España) y Americano (conocido por latinos), explícalas.
                3. Crear 3 ejemplos prácticos que validen su conocimiento previo pero corrijan el error.
            """),
            expected_output=dedent("""
                Un plan de micro-lección de inglés:
                - Alerta de Error Común (L1 Interference).
                - Comparativa UK vs US (si aplica).
                - 3 Ejercicios correctivos explicados.
            """),
            agent=agent
        )

    def sintesis_guia_docente_task(self, agent, tema, materia):
        return Task(
            description=dedent(f"""
                Recopila el análisis realizado por el agente especialista en {materia} sobre '{tema}'.
                
                Tu tarea es estructurar toda esa información en una 'Ficha Docente Puente Cultural' final.
                Debe ser un documento listo para que el profesor lo imprima o lea en clase.
                Debe tener un tono alentador, profesional y muy claro.
            """),
            expected_output=dedent("""
                DOCUMENTO FINAL: FICHA DOCENTE PUENTE CULTURAL
                
                1. TÍTULO DEL TEMA
                2. OBJETIVO DE INCLUSIÓN (¿Por qué adaptamos esto?)
                3. PUENTES CULTURALES (Las analogías clave)
                4. VOCABULARIO Y CONTEXTO (Glosario explicado)
                5. ACTIVIDAD SUGERIDA (Dinámica rápida de 10 min)
                
                (Formato Markdown limpio y bien estructurado)
            """),
            agent=agent
        )