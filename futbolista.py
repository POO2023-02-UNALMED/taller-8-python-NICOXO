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

    def get_goles_marcados(self):
        return self.goles_marcados

    def set_goles_marcados(self, goles_marcados):
        self.goles_marcados = goles_marcados

    def get_tarjetas_rojas(self):
        return self.tarjetas_rojas

    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.tarjetas_rojas = tarjetas_rojas

    def get_pierna_habil(self):
        return self.pierna_habil

    def set_pierna_habil(self, pierna_habil):
        self.pierna_habil = pierna_habil

    def __str__(self):
        return f"Mi nombre es {self.get_nombre()} soy profesional en el deporte {self.get_deporte()} Tengo {self.get_edad()} años de edad y llevo {self.get_años_practicando()} años en el deporte"

