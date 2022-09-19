from zooAnimales.animal import Animal

class Mamifero(Animal):
    __listado=[]
    caballos=0
    leones=0

    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        Animal.mamiferos=Animal.mamiferos+1
        self.__pelaje=pelaje
        self.__patas=patas
        self.__listado.append(self)

    def isPelaje(self):
        return self.__pelaje

    def setPelaje(self,pelaje):
        self.__pelaje=pelaje

    def getPatas(self):
        return self.__patas

    def setPatas(self,patas):
        self.__patas=patas

    def cantidadMamiferos(self):
        return len(self.__listado)
    
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        cls.caballos+=1
        return Mamifero(nombre,edad,"pradera",genero,True,4)

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        cls.leones+=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    