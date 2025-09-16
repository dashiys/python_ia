class figurasGeometricas:
    def __init__(self,coordenadas):
        self.setCoordenadas(coordenadas)
        
    def setCoordenadas(self, coordenadas):
        self.__coordenadas= coordenadas
        
    def getCoordenadas(self):
        return self.__coordenadas