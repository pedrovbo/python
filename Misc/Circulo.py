class Circulo:

    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo._total_circulos += 1


    def get_total_circulos(self):
        return self._total_circulos