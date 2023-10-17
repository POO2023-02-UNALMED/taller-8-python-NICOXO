class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.sexo = sexo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo


class Deportista:
    def __init__(self, deporte="Futbol", años_practicando=0):
        self.deporte = deporte
        self.años_practicando = años_practicando

    def get_deporte(self):
        return self.deporte

    def set_deporte(self, deporte):
        self.deporte = deporte

    def get_años_practicando(self):
        return self.años_practicando

    def set_años_practicando(self, años_practicando):
        self.años_practicando = años_practicando


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

