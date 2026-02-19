from app.agents.crew import GeneradorContenidoCrew

# Simulación de una petición de un profesor
print("--- INICIANDO SIMULACIÓN PUENTE CULTURAL ---")

tema_prueba = "La Guerra Civil Española"
materia_prueba = "Historia"
perfil_prueba = "Mayoría de estudiantes de Colombia y Venezuela"

print(f"Tema: {tema_prueba}")
print(f"Materia: {materia_prueba}")
print(f"Perfil: {perfil_prueba}")
print("---------------------------------------------")

generador = GeneradorContenidoCrew(tema_prueba, materia_prueba, perfil_prueba)
resultado = generador.run()

print("\n\n################ RESULTADO FINAL ################\n")
print(resultado)