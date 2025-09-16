from FigurasGeometricas import figurasGeometricas

class circulo(figurasGeometricas):

    def __init__(self, cRadio, coordenadas):
        figurasGeometricas.__init__(self, coordenadas)
        self.SetRadio(cRadio)
        

    def SetRadio(self, cRadio):
        self.__cRadio = cRadio

    def GetRadio(self):
        return self.__cRadio

    def CalcularArea(self):
        area = round(3.1416 * (self.GetRadio() * self.GetRadio()), 2)
        return area

    def CalcularPerimetro(self):
        perimetro = round(2 * 3.1416 * self.GetRadio(), 2)
        return perimetro
        
    def __str__(self):
        return f"x: {self.GetX()} y: {self.GetY()}"