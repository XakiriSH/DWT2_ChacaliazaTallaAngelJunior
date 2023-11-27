import pickle

class Alumno:
    def __init__(self, nombre, apellido, edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nacionalidad = nacionalidad
    
    def leerNota(self):
        return self.nota

    def registrarNota(self, notaAlumno):
        #Validamos nota
        if 0 <= notaAlumno <= 20:
            self.nota = notaAlumno
            return True
        else:
            print("Error: La nota debe estar en el rango de 0 a 20")
            return False

#Guardamos archivo usando pickle
def guardar_alumnos(alumnos, archivo):
    with open(archivo, 'wb') as f:
        pickle.dump(alumnos, f)

#Cargamos datos
def cargar_alumnos(archivo):
    try:
        with open(archivo, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return[]