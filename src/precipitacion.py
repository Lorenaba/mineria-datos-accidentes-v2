import pandas as pd


class Precipitacion:

    def __init__(self, ruta):
        self.ruta = ruta
        self.df = None

    def cargar(self):
        self.df = pd.read_csv(self.ruta)
        return self.df