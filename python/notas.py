import csv

def cargarEvaluacion(nombreArchivo, puntajeMaximo, exigencia=60):
    evaluacion = []
    with open(nombreArchivo) as archivo:
        lector = csv.reader(archivo, delimiter=';')
        for fila in lector:
            alumno = {}
            alumno['nombre'] = fila[0]
            alumno['apellido'] = fila[1]
            puntos = [int(x) for x in fila[2:]]  # Obtener el puntaje obtenido 
            alumno['puntaje_total'] = sum(puntos)  # Sumar todos los puntos
            alumno['nota'] = calcularNota(alumno['puntaje_total'], puntajeMaximo)
            evaluacion.append(alumno)
    return evaluacion

def calcularNota(puntaje_total, puntaje_maximo):
    nota_maxima = 7  # Escala de 1 a 7
    nota = (puntaje_total / puntaje_maximo) * nota_maxima
    return round(max(1, min(nota, nota_maxima)), 2)


# Menu principal

print("--------'Carga de notas de evaluación----------")
nombreArchivo = input("Nombre del archivo (ejemplo: carpeta/nombrearchivo.csv):   ")
puntajeMaximo = int(input("Puntaje Máximo: "))
exigencia = int(input("Exigencia en %: "))
    
if 0 <= exigencia <= 100:
     evaluacion = cargarEvaluacion(nombreArchivo, puntajeMaximo, exigencia)
        
    # Imprime los resultados
for alumno in evaluacion:
            print(f"Nombre: {alumno['nombre']} {alumno['apellido']}")
            print(f"Puntaje Total Obtenido: {alumno['puntaje_total']}")
            print(f"Nota: {alumno['nota']}")
else:
    print("Error: La exigencia debe estar entre 0% y 100%.")
