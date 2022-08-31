class Monedero:

    MONEDA = "$"

    VALORES_MONEDAS = {
        "dolar": 1,
        "25ctvs": 0.25,
        "10ctvs": 0.10,
        "5ctvs": 0.05,
    }

    def __init__(self):
        self.ganacia = 0
        self.dinero_recibido = 0

    def reporte(self):
        """Imprime la ganacia"""
        print(f"Dinero: {self.MONEDA}{self.ganacia}")

    def procesar_monedas(self):
        """Retorna el dinero calculado de las monedas insertadas."""
        print("Por favor inserta las monedas.")
        for moneda in self.VALORES_MONEDAS:
            self.dinero_recibido += int(
                input(f"Cuantas monedas de {moneda}?: ")) * self.VALORES_MONEDAS[moneda]
        return self.dinero_recibido

    def hacer_pago(self, costo):
        """Returns True when payment is accepted, or False if insufficient."""
        self.procesar_monedas()
        if self.dinero_recibido >= costo:
            cambio = round(self.dinero_recibido - costo, 2)
            print(f"Aquí está tu cambio: {self.MONEDA}{cambio}$.")
            self.ganacia += costo
            self.dinero_recibido = 0
            return True
        else:
            print("Lo siento, el dinero insertado no es suficiente. Dinero devuelto.")
            self.dinero_recibido = 0
            return False
