from zooAnimales.animal import Animal

class Anfibio(Animal):
    __listado=[]
    ranas=0
    salamandras=0

    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        Animal.anfibios=Animal.anfibios+1
        self.__colorPiel=colorPiel
        self.__venenoso=venenoso
        self.__listado.append(self)

    def isVenenoso(self):
        return self.__venenoso

    def setVenenoso(self,venenoso):
        self.__venenoso=venenoso

    def getColorPiel(self):
        return self.__colorPiel

    def setColorPiel(self,colorPiel):
        self.__colorPiel=colorPiel

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        cls.ranas+=1
        return Anfibio(nombre,edad,"selva",genero,"rojo",True)

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        cls.salamandras+=1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)