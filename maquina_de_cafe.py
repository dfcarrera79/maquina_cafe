class MaquinaCafe:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leche": 200,
            "cafe": 100,
        }

    def reporte(self):
        """Imprime los recursos de la maquina."""
        print(f"Agua: {self.recursos['agua']} ml")
        print(f"Leche: {self.recursos['leche']} ml")
        print(f"Café: {self.recursos['cafe']} g")

    def recursos_suficientes(self, bebida):
        """Retorna True cuando la orden se puede hacer, False cuando los ingredientes son insuficientes"""
        se_puede_hacer = True
        for ingrediente in bebida.ingredientes:
            if bebida.ingredientes[ingrediente] > self.recursos[ingrediente]:
                print(f"Lo siento, no hay suficiente {ingrediente}.")
                se_puede_hacer = False
        return se_puede_hacer

    def hacer_cafe(self, orden):
        """Reduce los ingredientes requeridos de los recursos de la maquina."""
        for item in orden.ingredientes:
            self.recursos[item] -= orden.ingredientes[item]
        print(f"Aquí está tu {orden.nombre} ☕️. ¡Disfrútalo!")
