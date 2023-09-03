import paciente, historia_clinica
 
def salir():
    print("Gracias por usar el programa ...")
    exit()



def main():
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
        print("4.- Mostrar indicios cronicos")
        print("5.- Salir\n")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            paciente.registroPaciente()
        elif opcion == 2:
            historia_clinica.listarpacientes()
        elif opcion == 3:
            historia_clinica.buscarpaciente()
        elif opcion == 4: 
            historia_clinica.listasignos()
        elif opcion == 5:
            salir()


if __name__ == '__main__':
    main()
