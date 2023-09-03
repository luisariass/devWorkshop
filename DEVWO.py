lista_pacientes = {}

class Paciente(object):
    def __init__(self, _documento, _nombre, _sexo, _fecha_nacimiento, _presion, _temperatura, _saturacion, _frecuencia, _notas, _imagenes, _examenes, _medicamentos):
        self.documento = _documento
        self.nombre = _nombre
        self.sexo = _sexo
        self.fecha_nacimiento = _fecha_nacimiento
        self.presion = _presion
        self.temperatura = _temperatura
        self.saturacion = _saturacion
        self.frecuencia = _frecuencia
        self.notas = _notas
        self.imagenes = _imagenes
        self.examenes = _examenes
        self.medicamentos = _medicamentos
    
    def entregarDatos(self):
        print("\nDocumento: {}"
              "\nNombre: {} "
              "\nSexo: {}"
              "\nfecha nacimiento: {}"
              "\nPresion: {}"
              "\nTemperatura: {}"
              "\nSaturacion: {}"
              "\nFrecuencia: {}"
              "\nNotas de evolucion: {}"
              "\nImagenes diagnosticas: {}"
              "\nResultados examenes de laboratorio: {}"
              "\nMedicamentos formulados: {}\n".format(self.documento, self.nombre, self.sexo, self.fecha_nacimiento, self.presion, self.temperatura, self.saturacion, self.frecuencia,self.notas, self.imagenes, self.examenes, self.medicamentos))

    
def registroPaciente():
  print("\nRegistry de capacities\n")
  documento = int(input("digite el numero de documento del paciente: "))
  nombre = input("Ingress el name del patient: ")
  sexo = validarSexo(str(input("Ingress el sex del patient: ")))
  fecha_nacimiento = str(input("Ingress date of birth (DD/MM/AA): "))

  print("\nRegistro Signos vitales\n")
  presion_arterial = float(input("Ingrese la presion arterial del paciente: "))
  temperatura = float(input("ingrese la temperatura del paciente: "))
  saturacion = float(input("ingrese la saturacion O2 del paciente: "))
  frecuencia = float(input("ingrese la frecuencia respiratoria del paciente: "))
  
  print("\nRegistro de resultados\n")
  notas = str(input("ingrese las notas de evolucion del paciente: "))
  imagenes = int(input("ingrese el numero de imagenes diagnosticas del paciente: "))
  examenes = str(input("ingrese los resultados de los examenes de laboratorio "))
  medicamentos = str(input("ingrese los medicamentos formulados: "))

  paciente1 = Paciente(documento, nombre, sexo, fecha_nacimiento, presion_arterial, temperatura, saturacion, frecuencia, notas, imagenes, examenes, medicamentos)
  lista_pacientes.append(paciente1)


def listadoPacientes():
    cama = 300
    print("\nListado de pacientes\n")
    con = 0
    for paciente1 in lista_pacientes:
        con += 1
        print("Paciente {}".format(con))
        paciente1.entregarDatos()
    porcentaje = (con / cama) * 100
    print("hay {} pacientes de {} camas disponibles, ocupando un porcentaje de {} %: ".format(con, cama, porcentaje))


def buscarEstudiante():
  print("Buscar Estudiante\n")
  documento = int(input("Ingrese el numero de cedula a buscar: "))
  for paciente1 in lista_pacientes:
      if documento == paciente1.documento:
        paciente1.entregarDatos()
 
def validarSexo(x):
    while( x != 'f' and x != 'm'):
        print("\nError, vuelva a ingresar el sexo\n")
        x = str(input("Ingress el sex del patient: "))
    return x



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
        print("4.- Salir\n")

        opcion = int(input("Opcion: "))
        if opcion == 1:
            registroPaciente()
        elif opcion == 2:
            listadoPacientes()
        elif opcion == 3:
            buscarEstudiante()
        elif opcion == 4:
            salir()


if __name__ == '__main__':
    main()

# promedios de estancia por servicio,
# cantidad de admisiones y altas por servicio, 
# pacientes con enfermedades crónicas y prescripción de medicamentos por servicio.