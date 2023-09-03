
listaSignos = []
class medicamentos():
    def __init__(self, presure, temperature, hipo, frecuency) -> None:
        self. presure = presure
        self.temperature = temperature
        self.hipo = hipo
        self.frecuency = frecuency

    def entregarSignos(self):
        print(
            "\nPresion: {}"
            "\nTemperatura: {} "
            "\nSaturacion: {}"
            "\nFrecuencia: {}\n".format(self.presure, self.temperature, self.hipo, self.frecuency))
             
def validarSignos(presure,temperature,hipo,frecuency ):
    
    mensaje1 = "presion normal\n"
    mensaje1 = "Tiene indicios de hipertension " if presure > 140 else mensaje1
    mensaje1 = "Tiene indicios de hipotension " if presure < 90 else mensaje1

    mensaje2 = "Temperatura normal\n"
    mensaje2 = "Tiene indicios de hipotermia " if temperature < 35 else mensaje2
    mensaje2 = "Tiene indicios de hipertermia " if temperature > 38 else mensaje2 

    mensaje3 = "Saturacion oxigeno normal\n"
    mensaje3 = "Tiene indicios de hipoxemia " if hipo < 90 else mensaje3
    mensaje3 = "Tiene indicios de hiperoxia " if hipo > 100 else mensaje3

    mensaje4 = "Frecuencia respiratoria normal\n"
    mensaje4 = "Tiene indicios de bradipnea " if frecuency < 12 else mensaje4
    mensaje4 = "Tiene indicios de taquipnea " if frecuency > 20 else mensaje4
    
    paciente2 = medicamentos(mensaje1, mensaje2, mensaje3, mensaje4)
    listaSignos.append(paciente2)


