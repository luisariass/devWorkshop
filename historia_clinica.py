from paciente import listPatient
from medicamentos import listSigns


class History_clinical:


    @staticmethod
    def patient_list():
        bed = 300
        print("\nList patient\n")
        if len(listPatient) == 0:
            print("no patient mistakes\n")
        con = 0
        for patient1 in listPatient:
            con += 1
            print("Patient {}".format(con))
            patient1.deliverData()
        percentage = (con / bed) * 100
        print("there are {} patients out of {} beds available, occupying a percentage of {} %: ".format(con, bed, percentage))

    @staticmethod
    def search_patient():
        print("\nSearch patient\n")
        if len(listPatient) == 0:
            print("no patient mistakes")
            return
        document = int(input("enter the ID number to search: "))
        for patient1 in listPatient:
            if document == patient1.id:
                patient1.deliverData()

    @staticmethod
    def list_signs():
        cont = 0
        print("\nlist Vital signs ")
        if len(listSigns) == 0:
            print("no patient mistakes\n")
        for patient2 in listSigns:
            cont += 1
            print("\n")
            print("Patient {}".format(cont))
            patient2.entregarSignos()
