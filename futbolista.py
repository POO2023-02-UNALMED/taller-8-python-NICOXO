from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, Nombre, edad, altura, sexo, deporte="Futbol", añosPracticando=0, golesMarcados=0,
                 tarjetasRojas=0, piernaHabil=""):
        Persona.__init__(self, Nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        self.golesMarcados = golesMarcados
        self.tarjetasRojas = tarjetasRojas
        self.piernaHabil = piernaHabil

        Futbolista.listaFutbolistas.append(self)

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getAltura(self):
        return self.altura

    def getSexo(self):
        return self.sexo

    def getAñosPracticando(self):
        return self.añosPracticando

    def getGolesMarcados(self):
        return self.golesMarcados

    def getTarjetasRojas(self):
        return self.tarjetasRojas

    def getPiernaHabil(self):
        return self.piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"

