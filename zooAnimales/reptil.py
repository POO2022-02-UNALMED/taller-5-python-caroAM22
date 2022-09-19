from zooAnimales.animal import Animal

class Reptil(Animal):
    __listado=[]
    serpientes=0
    iguanas=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        Animal.reptiles=Animal.reptiles+1
        self.__colorEscamas=colorEscamas
        self.__largoCola=largoCola
        self.__listado.append(self)

    def getColorEscamas(self):
        return self.__colorEscamas

    def setColorEscamas(self,colorEscamas):
        self.__colorEscamas=colorEscamas

    def getLargoCola(self):
        return self.__largoCola

    def setLargoCola(self,largoCola):
        self.__largoCola=largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        cls.iguanas+=1
        return Reptil(nombre,edad,"humedal",genero,"verde",3)

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        cls.serpientes+=1
        return Reptil(nombre,edad,"jungla",genero,"blanco",1)