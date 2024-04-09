import Estudiante

class Secretaria:


    def __init__(self, lista_estudiantes : list[Estudiante.Estudiante]) -> None:
        self.lista_estudiantes = lista_estudiantes


    def agregar_estudiante (self, Estudiante) -> None:
        self.lista_estudiantes.append(Estudiante)

    def borrar_estudiante(self, Estudiante:Estudiante.Estudiante) -> None:
        self.lista_estudiantes.remove(Estudiante)


    def buscar_por_id (self, id:int) -> Estudiante.Estudiante:
        for estudiante in self.lista_estudiantes:
            if (estudiante.id == id):
                return estudiante
            
    def mostrar_todo (self):

        for estudiante in self.lista_estudiantes:

            print(estudiante)