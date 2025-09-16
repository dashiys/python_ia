from FigurasGeometricas import figurasGeometricas

class cuadrado(figurasGeometricas):
    
    def __init__(self, cBase, cAltura, coordenadas):
        figurasGeometricas.__init__(self, coordenadas)
        self.SetBase(cBase)
        self.SetAltura(cAltura)
        
    def SetBase(self, cBase):
        self.__cBase = cBase

    def SetAltura(self, cAltura):
        self.__cAltura = cAltura

    def GetBase(self):
        return self.__cBase

    def GetAltura(self):
        return self.__cAltura

    def CalcularArea(self):
        area = round(self.GetBase() * self.GetAltura(), 2)
        return area 

    def CalcularPerimetro(self):
        perimetro = round(self.GetBase() * 2 + self.GetAltura() * 2, 2)
        return perimetro

    def __str__(self):
        return f"x: {self.GetX()} y: {self.GetY()}"