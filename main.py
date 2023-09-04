import patient
from historia_clinica import ClinicalHistory


def exit_program():
    print("Thanks for using the program...")

def main():
    history = ClinicalHistory()
    while True:
        print("\n")
        print("|********************************|")
        print("|**|        Bienvenidos           |**|")
        print("|**|   al hospital San Vicente    |**|")
        print("|********************************|")
        print("")
        print("Seleccione una de las siguientes opciones:")
        print("1.- Registrar Paciente")
        print("2.- Mostrar Pacientes")
        print("3.- Buscar Paciente")
        print("4.- Mostrar indicios crónicos de los pacientes")
        print("5.- Salir\n")

        option = int(input("Opción: "))
        if option == 1:
            patient.patient_registration()
        elif option == 2:
            history.patient_list()
        elif option == 3:
            history.search_patient()
        elif option == 4:
            history.list_signs()
        elif option == 5:
            exit_program()
            break

if __name__ == '__main__':
    main()
