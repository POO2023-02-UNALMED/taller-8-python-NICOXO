from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    lista_futbolistas = []

    def __init__(self, nombre, edad, altura, sexo, deporte="Futbol", años_practicando=0, goles_marcados=0,
                 tarjetas_rojas=0, pierna_habil=""):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, años_practicando)
        self.goles_marcados = goles_marcados
        self.tarjetas_rojas = tarjetas_rojas
        self.pierna_habil = pierna_habil

        Futbolista.lista_futbolistas.append(self)

    def getNombre(self):
        return self.nombre

    def getGolesMarcados(self):
        return self.goles_marcados

    def setGolesMarcados(self, goles_marcados):
        self.goles_marcados = goles_marcados

    def getTarjetasRojas(self):
        return self.tarjetas_rojas

    def setTarjetasRojas(self, tarjetas_rojas):
        self.tarjetas_rojas = tarjetas_rojas

    def getPiernaHabil(self):
        return self.pierna_habil

    def setPiernaHabil(self, pierna_habil):
        self.pierna_habil = pierna_habil

    def __str__(self):
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"

