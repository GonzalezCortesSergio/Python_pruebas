import Estudiante

juan = Estudiante.Estudiante("Juan", 13, 1)
nombre = "Juan"
jose = Estudiante.Estudiante("Jose", 14, 2)

lista_estudiantes = [juan, jose]
nuevo_estudiante = Estudiante.Estudiante("Joselito", 14, 3)
lista_estudiantes.append(nuevo_estudiante)

for estudiante in lista_estudiantes:
    print(estudiante)

def buscar_por_nombre (nombre):

    for estudiante in lista_estudiantes:

        if (estudiante.nombre == nombre):
            return estudiante
        

print(buscar_por_nombre(nombre))


