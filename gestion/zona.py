class Zona:
    def __init__(self,nombre,zoo=None):
        self.__nombre=nombre
        self.__zoo=zoo
        self.__animales=[]

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

    def getZoo(self):
        return self.__zoo

    def setZoo(self,zoo):
        self.__zoo=zoo

    def getAnimales(self):
        return self.__animales

    def setAnimales(self,animales):
        return self.__animales

    def agregarAnimales(self,animal):
        self.__animales.append(animal)

    def cantidadAnimales(self):
        return len(self.__animales)