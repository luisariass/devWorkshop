from paciente import listadoPacientes
from medicamentos import listaSignos
class Historia_clinica():
    def __init__(self) -> None:
        pass


def listarpacientes():
    cama = 300
    print("\nListado de pacientes\n")
    if len(listadoPacientes) == 0:
        print("No hay pacientes registrados\n")
    con = 0
    for paciente1 in listadoPacientes:
        con += 1
        print("Paciente {}".format(con))
        paciente1.entregarDatos()
    porcentaje = (con / cama) * 100
    print("hay {} pacientes de {} camas disponibles, ocupando un porcentaje de {} %: ".format(con, cama, porcentaje))


def buscarpaciente():
    print("\nBuscar Paciente\n")
    if len(listadoPacientes) == 0:
        print("No hay pacientes registrados")
        return
    documento = int(input("Ingrese el numero de cedula a buscar: "))
    for paciente1 in listadoPacientes:
        if documento == paciente1.documento:
            paciente1.entregarDatos()

def listasignos():
    documento = int(input("Ingrese el numero de cedula a buscar: "))
    for paciente1 in listadoPacientes:
        for paciente2 in listaSignos:
            if documento == paciente1.documento:
                paciente2.entregarSignos()