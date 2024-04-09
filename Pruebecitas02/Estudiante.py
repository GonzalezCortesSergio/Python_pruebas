class Estudiante:
    

    def __init__(self, nombre: str, apellidos: str, edad: int, id):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.id = id


    def __str__(self) -> str:
        return "Estudiante: [ Nombre: " + self.nombre + ", Apellidos: " + self.apellidos + ", Edad: " + str(self.edad) + ", ID: " + str(self.id) + " ]"
    