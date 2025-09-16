from FigurasGeometricas import figurasGeometricas

class trianguloRectangulo(figurasGeometricas):

    def __init__(self, tBase, tAltura, coordenadas):
        figurasGeometricas.__init__(self, coordenadas)
        self.SetBase(tBase)
        self.SetAltura(tAltura)

    def SetBase(self, tBase):
        self.__tBase = tBase

    def SetAltura(self, tAltura):
        self.__tAltura = tAltura

    def GetBase(self):
        return self.__tBase

    def GetAltura(self):
        return self.__tAltura

    def CalcularArea(self):
        area = round((self.GetBase() * self.GetAltura()) / 2, 2)
        return area
    
    def CalcularPerimetro(self):
        hipotenusa = (self.GetBase() ** 2 + self.GetAltura() ** 2) ** (1 / 2)
        perimetro = round(self.GetBase() + self.GetAltura() + (hipotenusa), 1)
        return perimetro
    
    def __str__(self):
        return f"x: {self.GetX()} y: {self.GetY()}"