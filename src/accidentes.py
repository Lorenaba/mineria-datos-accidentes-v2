import pandas as pd


class Accidentes:

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
        # Copia de seguridad para trabajar sobre los datos
        self.df = self.df.copy()

        # Completar valores faltantes según la gravedad del accidente
        self.df.loc[
            self.df["GRAVEDAD_ACCIDENTE"] == "Solo daños",
            "CANT_HERIDOS_EN _SITIO_ACCIDENTE"
        ] = self.df.loc[
            self.df["GRAVEDAD_ACCIDENTE"] == "Solo daños",
            "CANT_HERIDOS_EN _SITIO_ACCIDENTE"
        ].fillna(0)

        self.df.loc[
            self.df["GRAVEDAD_ACCIDENTE"] == "Solo daños",
            "CANT_MUERTOS_EN _SITIO_ACCIDENTE"
        ] = self.df.loc[
            self.df["GRAVEDAD_ACCIDENTE"] == "Solo daños",
            "CANT_MUERTOS_EN _SITIO_ACCIDENTE"
        ].fillna(0)

        self.df.loc[
            self.df["GRAVEDAD_ACCIDENTE"] == "Con heridos",
            "CANT_MUERTOS_EN _SITIO_ACCIDENTE"
        ] = self.df.loc[
            self.df["GRAVEDAD_ACCIDENTE"] == "Con heridos",
            "CANT_MUERTOS_EN _SITIO_ACCIDENTE"
        ].fillna(0)

        return self.df

    def guardar(self, ruta_salida):
        self.df.to_csv(
            ruta_salida,
            index=False,
            encoding="utf-8-sig"
        )
        print("Archivo limpio guardado correctamente.")