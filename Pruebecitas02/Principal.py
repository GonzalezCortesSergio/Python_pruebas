#Variables

import Estudiante
import Secretaria


nombre:str
apellidos:str
edad:int
id:int = 1
salir = False

lista_estudiantes = [Estudiante.Estudiante("Sergio", "González Cortés", 18, id)]
secretaria = Secretaria.Secretaria(lista_estudiantes)

while (not salir):
    
    
    opc = int(input("""

        Opción 1:   Agregar alumno
        Opción 2:   Ver alumnos
        Opción 3:   Eliminar alumno
        Opción 0:   Salir
          
          """))

    if opc == 1:
        id+= 1
        nombre = input("Nombre del alumno: ")
        apellidos = input("Apellidos: ")
        edad = int(input("Edad del alumno: "))

        secretaria.agregar_estudiante(Estudiante.Estudiante(nombre, apellidos, edad, id))
        


    elif opc == 2:

        secretaria.mostrar_todo()


    elif opc == 3:

        id = int(input("ID del alumno que quieres eliminar: "))

        secretaria.borrar_estudiante(secretaria.buscar_por_id(id))

    elif opc == 0:

        salir = True
        break


print("Gracias por utilizar el programa")

    

    



            