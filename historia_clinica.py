from patient import listPatient
from medicamentos import listSigns


class ClinicalHistory:
    @staticmethod
    def patient_list():
        bed = 300
        print("\nList of Patients\n")
        if len(listPatient) == 0:
            print("No patient records\n")
            return
        con = 0
        for patient1 in listPatient:
            con += 1
            print("Patient {}".format(con))
            patient1.deliverData()
        percentage = (con / bed) * 100
        print("There are {} patients out of {} available beds, occupying a percentage of {}%.".format(con, bed,
                                                                                                        percentage))

    @staticmethod
    def search_patient():
        print("\nSearch for a Patient\n")
        if len(listPatient) == 0:
            print("No patient records")
            return
        document = int(input("Enter the ID number to search: "))
        for patient1 in listPatient:
            if document == patient1.id:
                patient1.deliverData()

    @staticmethod
    def list_signs():
        cont = 0
        print("\nList of Vital Signs")
        if len(listSigns) == 0:
            print("No vital signs records\n")
            return
        for patient2 in listSigns:
            cont += 1
            print("\n")
            print("Patient {}".format(cont))
            patient2.deliverSigns()
