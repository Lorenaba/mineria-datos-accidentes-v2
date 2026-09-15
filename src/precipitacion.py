import pandas as pd


class Precipitacion:

    def __init__(self, ruta):
        self.ruta = ruta
        self.df = None

    def cargar(self):
        self.df = pd.read_csv(self.ruta)
        return self.df

    def diagnosticar(self):
        print("Filas:", len(self.df))
        print("Columnas:", len(self.df.columns))
        print("\nValores nulos:")
        print(self.df.isnull().sum())
        print("\nDuplicados:", self.df.duplicated().sum())

    def limpiar(self):
        self.df = self.df.copy()

        self.df["fechaobservacion"] = pd.to_datetime(
            self.df["fechaobservacion"],
            errors="coerce"
        )

        return self.df

    def guardar(self, ruta_salida):
        self.df.to_csv(
            ruta_salida,
            index=False,
            encoding="utf-8-sig"
        )
        print("Archivo limpio guardado correctamente.")