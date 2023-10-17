class Deportista:
    def __init__(self, deporte="Futbol", añosPracticando=0):
        self.deporte = deporte
        self.añosPracticando = añosPracticando

    def get_deporte(self):
        return self.deporte

    def set_deporte(self, deporte):
        self.deporte = deporte

    def get_añosPracticando(self):
        return self.añosPracticando

    def set_añosPracticando(self, añosPracticando):
        self.añosPracticando = añosPracticando