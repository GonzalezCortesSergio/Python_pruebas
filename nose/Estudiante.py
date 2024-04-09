from typing import Any


class Estudiante:
    def __init__(self, nombre, edad, id):
        self.nombre = nombre
        self.edad = edad
        self.id = id

    def __str__(self) -> str:
        return "Estudiante: [Nombre: " + self.nombre + ", Edad: " + str(self.edad)  + ", ID: " + str(self.id) + " ]"

