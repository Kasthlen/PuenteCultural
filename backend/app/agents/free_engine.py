from textwrap import dedent


class FreeContentGenerator:
    def generate(self, tema: str, materia: str, perfil_alumnos: str) -> str:
        materia_normalizada = (materia or "").strip().lower()

        if materia_normalizada == "historia":
            return self._historia(tema, perfil_alumnos)
        if materia_normalizada == "literatura":
            return self._literatura(tema, perfil_alumnos)
        if materia_normalizada == "ingles":
            return self._ingles(tema, perfil_alumnos)

        return dedent(
            f"""
            # FICHA DOCENTE PUENTE CULTURAL

            ## 1. TÍTULO DEL TEMA
            {tema}

            ## 2. OBJETIVO DE INCLUSIÓN
            Facilitar la comprensión del contenido para el perfil: {perfil_alumnos}.

            ## 3. PUENTES CULTURALES
            - Relacionar el tema con procesos sociales y políticos conocidos en Latinoamérica.
            - Activar conocimientos previos mediante ejemplos cercanos al contexto del grupo.

            ## 4. VOCABULARIO Y CONTEXTO
            - Contextualización histórica y social antes del contenido principal.
            - Glosario breve de términos clave para evitar barreras lingüísticas.

            ## 5. ACTIVIDAD SUGERIDA (10 MIN)
            Pregunta disparadora + comparación guiada + mini cierre reflexivo.

            ---
            _Generado en modo gratuito local (sin consumo de API)._ 
            """
        ).strip()

    def _historia(self, tema: str, perfil_alumnos: str) -> str:
        return dedent(
            f"""
            # FICHA DOCENTE PUENTE CULTURAL

            ## 1. TÍTULO DEL TEMA
            {tema}

            ## 2. OBJETIVO DE INCLUSIÓN
            Conectar procesos de conflicto político y memoria histórica de España con referentes comprensibles para estudiantes de {perfil_alumnos}.

            ## 3. PUENTES CULTURALES (ANALOGÍAS)
            | Hecho en España | Puente con Colombia | Puente con Venezuela |
            |---|---|---|
            | Polarización ideológica (1931-1936) | Tensiones entre proyectos de país en distintos periodos del siglo XX y XXI | Polarización política y social en las últimas décadas |
            | Guerra civil y fractura social | Impacto prolongado del conflicto armado interno en familias y territorios | Fracturas sociales por crisis política, económica y migratoria |
            | Dictadura franquista y control político | Debates sobre seguridad, libertades y memoria de víctimas | Debates sobre institucionalidad, derechos y participación democrática |

            ## 4. VOCABULARIO Y CONTEXTO
            - **República:** forma de Estado sin monarquía hereditaria.
            - **Bando sublevado:** grupo militar y político que se levantó contra el gobierno republicano.
            - **Frente Popular:** coalición electoral de izquierdas en 1936.
            - **Retaguardia:** zona alejada del frente de batalla.
            - **Exilio:** salida forzada del país por persecución política.
            - **Memoria histórica:** trabajo social e institucional para reconocer víctimas y explicar el pasado.

            ## 5. ACTIVIDAD SUGERIDA (10 MIN)
            1. **Minuto 1-2:** pregunta inicial: “¿Qué pasa cuando una sociedad se polariza y deja de dialogar?”.
            2. **Minuto 3-6:** comparación guiada en parejas (España vs Colombia/Venezuela).
            3. **Minuto 7-10:** cierre con una idea clave por pareja sobre prevención de violencia política.

            ---
            _Generado en modo gratuito local (sin consumo de API)._ 
            """
        ).strip()

    def _literatura(self, tema: str, perfil_alumnos: str) -> str:
        return dedent(
            f"""
            # FICHA DOCENTE PUENTE CULTURAL

            ## 1. TÍTULO DEL TEMA
            {tema}

            ## 2. OBJETIVO DE INCLUSIÓN
            Reducir barreras de comprensión literaria para estudiantes de {perfil_alumnos}, conectando la obra con experiencias universales.

            ## 3. PUENTES CULTURALES
            - Honor, familia, justicia, migración, desigualdad y poder como temas compartidos.
            - Relación entre contexto histórico de la obra y realidades latinoamericanas.

            ## 4. VOCABULARIO Y CONTEXTO
            - Glosario de arcaísmos y expresiones peninsulares complejas.
            - Parafraseo en español actual latino para fragmentos difíciles.
            - Contexto del autor, época y conflicto central antes de la lectura.

            ## 5. ACTIVIDAD SUGERIDA (10 MIN)
            Lectura breve + traducción cultural colaborativa + pregunta de conexión personal.

            ---
            _Generado en modo gratuito local (sin consumo de API)._ 
            """
        ).strip()

    def _ingles(self, tema: str, perfil_alumnos: str) -> str:
        return dedent(
            f"""
            # FICHA DOCENTE PUENTE CULTURAL

            ## 1. TÍTULO DEL TEMA
            {tema}

            ## 2. OBJETIVO DE INCLUSIÓN
            Aprovechar el español como base para evitar interferencias frecuentes en estudiantes de {perfil_alumnos}.

            ## 3. PUENTES CULTURALES
            - Conectar la estructura nueva con ejemplos cotidianos del contexto latino.
            - Validar intuiciones del estudiante antes de corregir errores.

            ## 4. VOCABULARIO Y CONTEXTO
            - **False friends** frecuentes según tema (ej.: actually/currently, sensible/sensitive).
            - Diferencias UK/US cuando afecten evaluación o comprensión.
            - Frases modelo con contraste “error común vs forma correcta”.

            ## 5. ACTIVIDAD SUGERIDA (10 MIN)
            3 micro-ejercicios: detectar error, corregir en parejas y producir oración final correcta.

            ---
            _Generado en modo gratuito local (sin consumo de API)._ 
            """
        ).strip()