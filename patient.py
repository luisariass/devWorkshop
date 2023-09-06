from medicamentos import validateSigns  # Importa la función 'validateSigns' desde el módulo 'medicamentos'.
from cama import Cama  # Importa la clase 'Cama' desde el módulo 'cama'.
from datetime import datetime  # Importa la clase 'datetime' desde el módulo 'datetime'.

listPatient = []  # Inicializa una lista vacía para almacenar objetos de pacientes.

object_bed = Cama()  # Crea una instancia de la clase 'Cama' llamada 'object_bed'.

# Define la clase 'Patient'.
class Patient(object):
    def __init__(self, _id, _name, _sex, _birthdate, _pressure, _temperature, _saturation, _frequency, _notes, _image, _exam, _medicines):
        """
        Constructor para Patient.

        Args:
            _id (int): Número de documento del paciente.
            _name (str): Nombre del paciente.
            _sex (str): Género del paciente ('M' o 'F').
            _birthdate (datetime): Fecha de nacimiento del paciente.
            _pressure (int): Presión arterial sistólica del paciente.
            _temperature (float): Temperatura del paciente en grados Celsius.
            _saturation (float): Saturación de oxígeno del paciente en porcentaje.
            _frequency (float): Frecuencia respiratoria del paciente en segundos.
            _notes (str): Nota de progreso del paciente.
            _image (str): Código de imagen de diagnóstico del paciente.
            _exam (str): Resultados de los exámenes de laboratorio del paciente.
            _medicines (str): Medicamentos recetados para el paciente.
        """
        self.id = _id
        self.name = _name
        self.sex = _sex
        self.birthdate = _birthdate
        self.pressure = _pressure
        self.temperature = _temperature
        self.saturation = _saturation
        self.frequency = _frequency
        self.notes = _notes
        self.image = _image
        self.exam = _exam
        self.medicines = _medicines

    def deliverData(self):
        # Muestra los datos del paciente formateados.
        print(f"\nDocument: {self.id}"
              f"\nName: {self.name}"
              f"\nSex: {self.sex}"
              f"\nBirthdate: {self.birthdate}"
              f"\nPressure: {self.pressure}"
              f"\nTemperature: {self.temperature}"
              f"\nSaturation: {self.saturation}"
              f"\nFrequency: {self.frequency}"
              f"\nNotes Evolution: {self.notes}"
              f"\nImages Diagnostic: {self.image}"
              f"\nResultants Exam Laboratory: {self.exam}"
              f"\nMedicines Formulas: {self.medicines}\n")

# Define la función para registrar pacientes.
def patient_registration():
    print("\nRegistry of Capacities")
    print("-" * 80)
    document = int(input("Enter the patient's document number: "))
    name = input("Enter the patient's name: ")
    sex = validate_gender(input("Enter the patient's gender (m/f): "))
    birthdate = validate_birthdate(input("Enter date of birth (YYYY-MM-DD): "))

    print("\nRegistry of Vital Signs")
    print("-" * 80)
    pressure_arterial = float(input("Enter the patient's blood pressure: "))
    temperature = float(input("Enter the patient's temperature: "))
    saturation = float(input("Enter the patient's O2 saturation: "))
    frequency = float(input("Enter the patient's respiratory rate: "))
    validateSigns(pressure_arterial, temperature, saturation, frequency)

    print("\nRegistry of Results")
    print("-" * 80)
    notes = input("Enter the patient's progress notes: ")
    image = input("Enter the number of diagnostic images of the patient: ")
    exam = input("Enter the results of laboratory tests: ")
    medicines = input("Enter the prescribed medicines: ")

    patient1 = Patient(document, name, sex, birthdate, pressure_arterial, temperature, saturation, frequency, notes,
                       image, exam, medicines)
    listPatient.append(patient1)

    estancia = int(input("Is the patient still in the clinic? (1 = yes, 2 = no): "))
    object_bed.calculateOcupation(estancia)  # Llama al método 'calculateOcupation' de 'object_bed'.

    print("\nPatient {} has been successfully registered\n".format(name))

# Define la función para validar el género del paciente.
def validate_gender(x):
    while x != 'f' and x != 'm':
        print("\nError, please re-enter gender (m/f)\n")
        x = input("Enter the patient's gender (m/f): ")
    return x

# Define la función para validar la fecha de nacimiento del paciente.
def validate_birthdate(date_str):
    while True:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")  # Intenta analizar la fecha en el formato especificado.
            break
        except ValueError:
            print("Error, please use the format (YYYY-MM-DD).")
            date_str = input("Enter date of birth (YYYY-MM-DD): ")
            return date_str