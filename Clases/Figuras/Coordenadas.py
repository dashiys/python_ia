class coordenadas:

    def __init__(self, PosicionX, PosicionY):
        self.SetX(PosicionX)
        self.SetY(PosicionY)

    def SetX(self, PosicionX):
        self.__PosicionX = PosicionX

    def SetY(self, PosicionY):
        self.__PosicionY = PosicionY

    def GetX(self):
        return self.__PosicionX

    def GetY(self):
        return self.__PosicionY
    
    def __str__(self):
        return f"x: {self.GetX()} y:{self.GetY()}"