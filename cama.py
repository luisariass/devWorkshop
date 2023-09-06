lista = []  # Lista vacía para almacenar porcentajes de ocupación.
listaHay = []  # Lista vacía para contar pacientes registrados.
listanohay = []  # Lista vacía para contar pacientes dados de alta.

class Cama:
    @staticmethod 
    def calculateOcupation(estancia):
        hay = 0  # Inicializa la variable hay (pacientes en el hospital).
        nohay = 0  # Inicializa la variable nohay (pacientes dados de alta).
        bed = 300  # Número total de camas en el hospital.

        if estancia == 1:
            hay += 1  # Incrementa el número de pacientes en el hospital.
            listaHay.append(hay)  # Agrega el número de pacientes a la lista de pacientes registrados.
            percentage = (hay / bed) * 100  # Calcula el porcentaje de ocupación.
            lista.append(percentage)  # Agrega el porcentaje a la lista de porcentajes de ocupación.
        elif estancia == 2:
            nohay += 1  # Incrementa el número de pacientes dados de alta.
            listanohay.append(nohay)  # Agrega el número de pacientes dados de alta a la lista.

        suma = sum(lista)  # Calcula la suma de los porcentajes de ocupación.
        x = len(listaHay)  # Obtiene el número de pacientes registrados.
        y = len(listanohay)  # Obtiene el número de pacientes dados de alta.

        # Imprime información sobre la ocupación del hospital.
        print(f"\nHay {estancia} pacientes registrados en el hospital")
        print(f"\nHay {x} pacientes de {bed} disponibles, con un porcentaje de ocupación de {suma} %")
        print(f"\nHay {y} pacientes que fueron dados de alta")