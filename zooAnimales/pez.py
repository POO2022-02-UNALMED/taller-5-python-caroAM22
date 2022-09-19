from zooAnimales.animal import Animal

class Pez(Animal):
    __listado=[]
    salmones=0
    bacalaos=0

    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        Animal.peces=Animal.peces+1
        self.__colorEscamas=colorEscamas
        self.__cantidadAletas=cantidadAletas
        self.__listado.append(self)

    def getColorEscamas(self):
            return self.__colorEscamas

    def setColorEscamas(self,colorEscamas):
        self.__colorEscamas=colorEscamas

    def getCantidadAletas(self):
        return self.__cantidadAletas

    def setPatas(self,cantidadAletas):
        self.__cantidadAletas=cantidadAletas

    @classmethod
    def cantidadPeces(cls):
        return len(cls.__listado)
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        cls.salmones+=1
        return Pez(nombre,edad,"oceano",genero,"rojo",6)

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        cls.bacalaos+=1
        return Pez(nombre,edad,"oceano",genero,"gris",6)