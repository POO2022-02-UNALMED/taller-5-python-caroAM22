class Animal:
    __totalAnimales=0

    def __init__(self,nombre,edad,habitat,genero):
        self.__nombre=nombre
        self.__edad=edad
        self.__habitat=habitat
        self.__genero=genero
        self.__zona=[]

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self,edad):
        self.__edad=edad

    def getHabitat(self):
        return self.__habitat

    def setHabitat(self,habitat):
        self.__habitat=habitat

    def getGenero(self):
        return self.__genero

    def setGenero(self,genero):
        self.__genero=genero

    def getZona(self):
        return self.__zona

    def setZona(self,zona):
        self.__zona=zona

    def getTotalAnimales(self):
        return self.__totalAnimales

    def setNombre(self,totalAnimales):
        self.__totalAnimales=totalAnimales

    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos: " + cls.cantidadMamiferos()+"\n"+"Aves: " + cls.cantidadAves()+"\n"+"Reptiles: " + cls.cantidadReptiles()+"\n"+"Peces: " + cls.cantidadPeces()+"\n"+"Anfibios: "+ cls.cantidadAnfibios()

    def toString(self):
        if self.__zona!=[] and self.__zona[0].__getZoo()!=None:
            return "Mi nombre es "+ self.__nombre+", tengo una edad de "+ str(self.__edad) +", habito en "+ self.__habitat+ " y mi genero es "+ self.__genero+",la zona en la que me ubico es "+ self.__zona[0]+", en el "+ self.__zona[0].getZoo()
        else:
            return "Mi nombre es "+ self.__nombre+", tengo una edad de "+ str(self.__edad) +", habito en "+ self.__habitat+ " y mi genero es "+ self.__genero