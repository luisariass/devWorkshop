from medicamentos import validateSigns
from datetime import date

listPatient = []


class Paciente(object):
    def __init__(self, _id, _name, _sex, _birthdate, _pressure, _temperature, _saturation, _frecuency, _notes, _image, _exam, _medicines):
        self.id = _id
        self.name = _name
        self.sex = _sex
        self.birthdate = _birthdate
        self.pressure = _pressure
        self.temperature = _temperature
        self.saturation = _saturation
        self.frecuency = _frecuency
        self.notes = _notes
        self.image = _image
        self.exam = _exam
        self.medicines = _medicines

    def deliverData(self):
        print(f"\nDocument: {self.id}"
              f"\nName: {self.name} "
              f"\nSex: {self.sex}"
              f"\nBirthdate: {self.birthdate}"
              f"\npressure: {self.pressure}"
              f"\ntemperature: {self.pressure}"
              f"\nsaturation: {self.saturation}"
              f"\nfrecuency: {self.frecuency}"
              f"\nNotas de evolucion: {self.notes}"
              f"\nImagenes diagnosticas: {self.image}"
              f"\nResultados examenes de laboratorio: {self.exam}"
              f"\nmedicines formulados: {self.medicines}\n")


def patient_registration():
    print("\nRegistry de capacities")
    print("-" * 80)
    id = int(input("Enter the patient's document number "))
    name = input("Ingress el name del patient: ")
    sex = validate_gender(str(input("Ingress el sex del patient: ")))
    birthdate = str(input("Ingress date of birth (DD/MM/AA): "))

    print("\nRegistry Vital signs")
    print("-" * 80)
    pressure_arterial = (float(input("Enter the patient's blood pressure: ")))
    temperature = (float(input("enter the patient's temperature: ")))
    saturation = float(input("enter the patient's O2 saturation: "))
    frecuency = float(input("enter the patient's respiratory rate: "))
    validateSigns(pressure_arterial, temperature, saturation, frecuency)

    print("\nRegistry of results")
    print("-" * 80)
    notes = str(input("enter the patient's progress notes: "))
    image = str(input("enter the number of diagnostic images of the patient: "))
    exam = str(input("enter the results of laboratory tests "))
    medicines = str(input("enter the prescribed medicines: "))

    patient1 = Paciente(id, name, sex, birthdate, pressure_arterial, temperature, saturation,frecuency, notes, image, exam, medicines)
    listPatient.append(patient1)

    print("\nPatient {} has been successfully registered\n".format(name))


def validate_gender(x):
    while x != 'f' and x != 'm':
        print("\nError, re-enter gender\n")
        x = str(input("Ingress el sex del patient: "))
    return x
