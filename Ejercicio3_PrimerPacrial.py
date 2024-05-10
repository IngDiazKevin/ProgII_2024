# Crear el diccionario de estudiantes
estudiantes = {
    1001: ("Juan", [85, 90, 88]),
    1002: ("María", [78, 85, 92]),
    1003: ("Pedro", [90, 92, 95]),
    1004: ("Ana", [88, 84, 90]),
    1005: ("Luis", [92, 91, 89])
}

# Función para calcular el promedio de un estudiante
def promedio_estudiante(id_estudiante):
    nombre, calificaciones = estudiantes[id_estudiante]
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

# Función para calcular el promedio general de todos los estudiantes
def promedio_general():
    total_calificaciones = []
    for estudiante in estudiantes.values():
        total_calificaciones.extend(estudiante[1])
    promedio = sum(total_calificaciones) / len(total_calificaciones)
    return promedio

# Función para encontrar al mejor estudiante (mayor promedio)
def mejor_estudiante():
    mejor_promedio = -1
    mejor_estudiante_id = None
    for id_estudiante, datos in estudiantes.items():
        promedio = promedio_estudiante(id_estudiante)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante_id = id_estudiante
    return mejor_estudiante_id

# Ejemplos de uso de las funciones
print("Promedio de María:", promedio_estudiante(1002))
print("Promedio general de todos los estudiantes:", promedio_general())
print("El mejor estudiante es:", mejor_estudiante())
