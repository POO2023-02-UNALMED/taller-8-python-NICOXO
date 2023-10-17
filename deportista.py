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