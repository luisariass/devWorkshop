listSigns = []


class medicament:
    def __init__(self, pressure, temperature, hippo, frequency) -> None:
        self.pressure = pressure
        self.temperature = temperature
        self.hippo = hippo
        self.frequency = frequency

    def deliverSigns(self):
        print(
            "-" * 20,
            "\nPressure: {}"
            "\nTemperature: {} "
            "\nSaturation: {}"
            "\nFrequency: {}".format(self.pressure, self.temperature, self.hippo, self.frequency))


def validateSigns(pressure, temperature, hippo, frequency):
    message1 = "Pressure normal"
    message1 = "Has signs of hypertension " if pressure > 140 else message1
    message1 = "Has signs of hypotension " if pressure < 90 else message1

    message2 = "Temperature normal"
    message2 = "Has signs of hypothermia " if temperature < 35 else message2
    message2 = "Has signs of hyperthermia " if temperature > 38 else message2

    message3 = "normal oxygen saturation "
    message3 = "Has signs of hypoxemia " if hippo < 90 else message3
    message3 = "Has signs of hyperoxia " if hippo > 100 else message3

    message4 = "Frecuencia respiratoria normal"
    message4 = "Has signs of bradypnea " if frequency < 12 else message4
    message4 = "Has signs of tachypnea " if frequency > 20 else message4
    # presion  #temperatura #saturacion #frecuencia
    patient2 = medicament(message1, message2, message3, message4)
    listSigns.append(patient2)
