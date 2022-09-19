from zooAnimales.animal import Animal

class Ave(Animal):
    __listado=[]
    aguilas=0
    halcones=0

    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self.__colorPlumas=colorPlumas
        self.__listado.append(self)

    def getColorPlumas(self):
        return self.__colorPlumas

    def setColorPlumas(self,colorPlumas):
        self.__colorPlumas=colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        cls.halcones+=1
        return Ave(nombre,edad,"montanas",genero,"cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        cls.aguilas+=1
        return Ave(nombre,edad,"montanas",genero,"blanco y amarillo")