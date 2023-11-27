from alumnos import Alumno, guardar_alumnos, cargar_alumnos

def registrar_alumnos():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    edad = int(input("Ingrese la edad del alumno: "))
    nacionalidad = input("Ingrese la nacionalidad del alumno: ")

    return Alumno(nombre, apellido, edad, 0, nacionalidad)

def main():

    alumnos = cargar_alumnos("alumnos.pkl")

    while True:
        #lista_alumnos = []
        print("*******************************")
        print("Bienvenido al registro de notas")
        print("*******************************")
        print("Ingrese comando")
        print("R: Registrar Alumno")
        print("C: Calificar Alumno")
        print("P: Promedio de Alumnos")
        print("S: Suma de notas de Alumnos")
        print("X: Finalizar")

        opcion = input("Seleccione una opcion: ")

        if opcion == 'R':
            alumno_nuevo = registrar_alumnos()
            alumnos.append(alumno_nuevo)
            print("Alumno registrado correctamente")
            
        elif opcion =='C':
            for alumno in alumnos:
                nota_valida = False
                while not nota_valida:
                    try:
                        nota = int(input(f"Ingrese nota para {alumno.nombre} {alumno.apellido}: "))
                        nota_valida = alumno.registrarNota(nota)
                    except ValueError:
                        print("Ingrese un número valido para la nota")

        elif opcion == 'P':
            promedio = sum(alumno.leerNota() for alumno in alumnos) / len(alumnos)
            print(f"El promedio de notas de todos los alumnos es: {promedio:.2f}")

        elif opcion == 'S':
            suma_notas = sum(alumno.leerNota() for alumno in alumnos)
            print(f"LA suma de notas de {len(alumnos)} alumnos es: {suma_notas}") 

        elif opcion == 'X':
            print("Saliendo del prorgrama")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()