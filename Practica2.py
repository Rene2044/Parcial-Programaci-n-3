def calcular_promedio(nombre, notas):
    promedio = sum(notas) / len(notas) if notas else 0
    return {
        "Estudiante": nombre,
        "Notas": notas,
        "Promedio": round(promedio, 2),
        "Estado": "Aprobado" if promedio >= 6 else "Reprobado"
    }

# Lista de estudiantes con sus notas
estudiantes = {
    "Ana": [7.5, 8.0, 6.5],
    "Luis": [5.0, 4.5, 6.0],
    "María": [9.0, 8.5, 9.5],
    "Carlos": [6.0, 6.0, 6.0]
}

# Procesar y mostrar resultados
for nombre, notas in estudiantes.items():
    resultado = calcular_promedio(nombre, notas)
    print(f"{resultado['Estudiante']}: Promedio = {resultado['Promedio']} → {resultado['Estado']}")