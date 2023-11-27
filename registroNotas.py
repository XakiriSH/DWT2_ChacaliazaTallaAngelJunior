import alumnos

def main():
    while True:
        lista_alumnos = []
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
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            edad = int(input("Ingrese la edad del alumno: "))
            nacionalidad = input("Ingrese la nacionalidad del alumno: ")

            alum = alumnos(nombre, apellido, edad,nota, nacionalidad)
            lista_alumnos.append(alum)
            
        elif opcion =='C':
            pass

        elif opcion == 'P':
            pass

        elif opcion == 'S':
            pass

        elif opcion == 'X':
            print("Saliendo del prorgrama")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()