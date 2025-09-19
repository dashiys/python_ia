class Billete:
    def __init__(self, cliente, asiento):
        self.setCliente(cliente)
        self.setAsiento(asiento)
        
    def setCliente(self, cliente):
        self.__cliente = cliente

    def setAsiento(self, asiento):
        self.__asiento = asiento

    def getCliente(self):
        return self.__cliente

    def getAsiento(self):
        return self.__asiento

    def __str__(self):
        return f"Billete - Persona: {self.__cliente}, Asiento: {self.__asiento}"
