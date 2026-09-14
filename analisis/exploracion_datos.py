import pandas as pd

RUTA_ACCIDENTES = "dataset/Accidentalidad_en_Barranquilla_20260830.csv"
RUTA_PRECIPITACION = "dataset/precipitacion_barranquilla.csv"
RUTA_COMPARENDOS = "dataset/Comparendos_Barranquilla.csv"

# Cargar los datasets
df_accidentes = pd.read_csv(RUTA_ACCIDENTES)
df_precipitacion = pd.read_csv(RUTA_PRECIPITACION)
df_comparendos = pd.read_csv(RUTA_COMPARENDOS)

# Dimensiones
print("ACCIDENTES")
print("Dimensiones:", df_accidentes.shape)

print("\nPRECIPITACIÓN")
print("Dimensiones:", df_precipitacion.shape)

print("\nCOMPARENDOS")
print("Dimensiones:", df_comparendos.shape)

# Tipos de datos
print("\nTIPOS DE DATOS")

for nombre, df in [
    ("ACCIDENTES", df_accidentes),
    ("PRECIPITACIÓN", df_precipitacion),
    ("COMPARENDOS", df_comparendos)
]:
    print(f"\n{nombre}:")
    print(dict(df.dtypes.astype(str)))
    
    
    print("Filas y columnas:")
print(df_comparendos.shape)

print("\nPrimeras filas:")
print(df_comparendos.head())

print("\nÚltima fecha:")
print(df_comparendos["fecha_comparendo"].max())

print("\nPrimera fecha:")
print(df_comparendos["fecha_comparendo"].min())

print("\nValores faltantes:")
print(df_comparendos.isna().sum())

print("\nDuplicados:")
print(df_comparendos.duplicated().sum())

print("Dimensiones:", df_comparendos.shape)