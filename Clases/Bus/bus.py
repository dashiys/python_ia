from billetes import Billete
from pasajeros import Pasajero

class Bus:
    numeroBuses = 0
    def __init__(self, asientos):
        self.__capacidad = asientos
        self.__billetes = []
        self.id = id(Bus)
        Bus.numeroBuses += 1

    def getBilletes(self):
        return len(self.__billetes)  
    
    def getCapacidad(self):
        return self.__capacidad    

    def comprarBillete(self, persona):
        if len(self.__billetes) < self.__capacidad:
            asiento = len(self.__billetes) + 1
            billete = Billete(persona, asiento)
            self.__billetes.append(billete)
            print(f"Billete vendido a {persona} para el asiento {asiento}")
        else:
            print("No hay asientos disponibles en el bus")

    def devolverBillete(self, cliente):
        for billete in self.__billetes:
            if billete.getCliente().getNombre().lower() == cliente.lower():
                self.__billetes.remove(billete)
                print(f"Billete de {cliente} devuelto. Asiento liberado.")
                for i, b in enumerate(self.__billetes, start = 1):
                    b = i
                return
        print(f"No se encontró un billete a nombre de {cliente}")

    def mostrarPasajeros(self):
        print("\nLista de pasajeros:")
        if not self.__billetes:
            print("El bus está vacío")
        else:
            for b in self.__billetes:
                print(b)
    
    def asientosLibres(self):
        return self.__capacidad - len(self.__billetes)