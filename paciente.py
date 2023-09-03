from medicamentos import validarSignos, listaSignos
listadoPacientes = []

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
    presion_arterial = (float(input("Ingrese la presion arterial del paciente: ")))
    temperatura = (float(input("ingrese la temperatura del paciente: ")))
    saturacion = float(input("ingrese la saturacion O2 del paciente: "))
    frecuencia = float(input("ingrese la frecuencia respiratoria del paciente: "))
    
    print("\nRegistro de resultados\n")
    notas = str(input("ingrese las notas de evolucion del paciente: "))
    imagenes = str(input("ingrese el numero de imagenes diagnosticas del paciente: "))
    examenes = str(input("ingrese los resultados de los examenes de laboratorio "))
    medicamentos = str(input("ingrese los medicamentos formulados: "))
    
    paciente1 = Paciente(documento, nombre, sexo, fecha_nacimiento, presion_arterial, temperatura, saturacion, frecuencia, notas, imagenes, examenes, medicamentos)
    paciente2 = validarSignos(presion_arterial, temperatura, saturacion, frecuencia)

    listadoPacientes.append(paciente1)
    listaSignos.append(paciente2)
    print("\nEl paciente {} ha sido registrado con exito\n".format(nombre))

def validarSexo(x):
    while( x != 'f' and x != 'm'):
        print("\nError, vuelva a ingresar el sexo\n")
        x = str(input("Ingress el sex del patient: "))
    return x

