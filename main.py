import patient  # Importa el módulo 'patient' que contiene funciones relacionadas con los pacientes.
from historia_clinica import ClinicalHistory  # Importa la clase 'ClinicalHistory' desde el módulo 'historia_clinica'.

def exit_program():
    """
    Imprime un mensaje de despedida y sale del programa.
    """
    print("Thanks for using the program...")

def main():
    history = ClinicalHistory()  # Crea una instancia de la clase 'ClinicalHistory' para gestionar el historial clínico.

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

        option = int(input("Opción: "))  # Lee la opción seleccionada por el usuario como un entero.
        if option == 1:
            patient.patient_registration()  # Llama a la función 'patient_registration' para registrar un paciente.
        elif option == 2:
            history.patient_list()  # Llama al método 'patient_list' de la instancia 'history' para mostrar la lista de pacientes.
        elif option == 3:
            history.search_patient()  # Llama al método 'search_patient' de la instancia 'history' para buscar un paciente.
        elif option == 4:
            history.list_signs()  # Llama al método 'list_signs' de la instancia 'history' para mostrar los signos vitales de los pacientes.
        elif option == 5:
            exit_program()  # Llama a la función 'exit_program' para salir del programa.
            break

if __name__ == '__main__':
    main()  # Llama a la función 'main' cuando se ejecuta el script como programa principal.

