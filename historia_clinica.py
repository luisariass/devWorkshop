from patient import listPatient  # Importa la lista de pacientes desde el módulo 'patient'.
from medicamentos import listSigns  # Importa la lista de signos vitales desde el módulo 'medicamentos'.

class ClinicalHistory:

    @staticmethod
    def patient_list():
        """
        Proporciona la lista de pacientes registrados en ese momento.
        """
        print("\nList of Patients\n")
        if len(listPatient) == 0:
            print("No patient records\n")  # Imprime un mensaje si no hay registros de pacientes.
            return
        con = 0
        for patient1 in listPatient:
            con += 1
            print("Patient {}".format(con))
            patient1.deliverData()  # Llama al método 'deliverData' del objeto 'patient1' para mostrar los datos del paciente.

    @staticmethod
    def search_patient():
        """
        Permite buscar a un paciente específico por su ID.
        """
        print("\nSearch for a Patient\n")
        if len(listPatient) == 0:
            print("No patient records")  # Imprime un mensaje si no hay registros de pacientes.
            return
        document = int(input("Enter the ID number to search: "))  # Solicita al usuario que ingrese el ID del paciente a buscar.
        for patient1 in listPatient:
            if document == patient1.id:
                patient1.deliverData()  # Llama al método 'deliverData' del objeto 'patient1' para mostrar los datos del paciente.

    @staticmethod
    def list_signs():
        """
        Proporciona la lista de signos vitales validados.
        """
        cont = 0
        print("\nList of Vital Signs")
        if len(listSigns) == 0:
            print("No vital signs records\n")  # Imprime un mensaje si no hay registros de signos vitales.
            return
        for patient2 in listSigns:
            cont += 1
            print("\n")
            print("Patient {}".format(cont))
            patient2.deliverSigns()  # Llama al método 'deliverSigns' del objeto 'patient2' para mostrar los signos vitales del paciente.
