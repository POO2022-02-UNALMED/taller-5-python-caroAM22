class Zoologico:
    def __init__(self,nombre,ubicacion):
        self.__nombre=nombre
        self.__ubicacion=ubicacion
        self.__zona=[]

    def agregarZonas(self,zona):
        self.__zona.append(zona)
        zona.__zoo=self

    def cantidadTotalAnimales(self):
        c=0
        for i in self.__zona:
            c+=i.cantidadAnimales()
        return c

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        self.__nombre=nombre

    def getUbicacion(self):
        self.__ubicacion

    def setUbicacion(self,ubicacion):
        self.__ubicacion=ubicacion

    def getZona(self):
        return self.__zona

    def setZona(self,zona):
        self.__zona=zona
    