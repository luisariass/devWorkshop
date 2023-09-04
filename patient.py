from medicamentos import validateSigns

listPatient = []


class Patient(object):
    def __init__(self, _id, _name, _sex, _birthdate, _pressure, _temperature, _saturation, _frequency, _notes, _image,
                 _exam, _medicines):
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


def patient_registration():
    print("\nRegistry of Capacities")
    print("-" * 80)
    document = int(input("Enter the patient's document number: "))
    name = input("Enter the patient's name: ")
    sex = validate_gender(input("Enter the patient's gender (m/f): "))
    birthdate = input("Enter date of birth (DD/MM/YY): ")

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

    print("\nPatient {} has been successfully registered\n".format(name))


def validate_gender(x):
    while x != 'f' and x != 'm':
        print("\nError, please re-enter gender (m/f)\n")
        x = input("Enter the patient's gender (m/f): ")
    return x