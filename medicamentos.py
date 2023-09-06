listSigns = []  # Lista vacía para almacenar objetos de signos vitales.

class Medicament:
    def __init__(self, pressure, temperature, hippo, frequency) -> None:
        """
        Constructor for Medicament.

        Args:
            pressure (int): Patient's systolic blood pressure.
            temperature (float): Patient's temperature in degrees Celsius.
            hippo (float): Patient's oxygen saturation in percentage.
            frequency (float): Patient's respiratory rate in seconds.
        """
        self.pressure = pressure
        self.temperature = temperature
        self.hippo = hippo
        self.frequency = frequency

    def deliverSigns(self):
        # Muestra los signos vitales del paciente formateados.
        print(
            "-" * 20,
            f"\nPressure: {self.pressure}"
            f"\nTemperature: {self.temperature} "
            f"\nSaturation: {self.hippo}"
            f"\nFrequency: {self.frequency}")

def validateSigns(pressure, temperature, hippo, frequency):
    """
    Provides validation of vital signs and returns a message indicating any signs of chronic disease.
    """
    # Comprueba la presión arterial
    message1 = "Pressure normal"
    message1 = "Has signs of hypertension " if pressure > 140 else message1
    message1 = "Has signs of hypotension " if pressure < 90 else message1

    # Comprueba la temperatura corporal
    message2 = "Temperature normal"
    message2 = "Has signs of hypothermia " if temperature < 35 else message2
    message2 = "Has signs of hyperthermia " if temperature > 38 else message2

    # Comprueba la saturación de oxígeno
    message3 = "Normal oxygen saturation"
    message3 = "Has signs of hypoxemia " if hippo < 90 else message3
    message3 = "Has signs of hypoxia " if hippo > 100 else message3

    # Comprueba la frecuencia respiratoria
    message4 = "Normal respiratory frequency"
    message4 = "Has signs of bradycardia " if frequency < 12 else message4
    message4 = "Has signs of tachycardia " if frequency > 20 else message4

    # Crea un objeto Medicament con los mensajes y lo agrega a la lista listSigns.
    patient2 = Medicament(message1, message2, message3, message4)
    listSigns.append(patient2)

# Ejemplo de uso:
# validateSigns(120, 37, 95, 15)
# Esto agregará un objeto Medicament a la lista listSigns con los mensajes correspondientes.
