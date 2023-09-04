import paciente
from historia_clinica import History_clinical
 
def salir():
    print("Thanks for used the program ...")
    exit()


def main():
    historia = History_clinical()
    while True:
        print("\n")
        print("|********************************|")
        print("|**|        Bienvenidos           |**|")
        print("|**|   al hospital San vicente    |**|")
        print("|********************************|")
        print("")
        print("Seleccione una de las siguientes opciones:")
        print("1.- Registrar Paciente")
        print("2.- Mostrar Pacientes")
        print("3.- Buscar Paciente")
        print("4.- Mostrar indicios cronicos de los pacientes")
        print("5.- Salir\n")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            paciente.patient_registration()
        elif opcion == 2:
            historia.patient_list()
        elif opcion == 3:
            historia.search_patient()
        elif opcion == 4: 
            historia.list_signs()
        elif opcion == 5:
            salir()


if __name__ == '__main__':
    main()