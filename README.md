# Minería de Datos - Accidentes de Tránsito en Barranquilla

## Descripción del proyecto

Este proyecto realiza un análisis de datos sobre los accidentes de tránsito registrados en Barranquilla, relacionándolos con información de precipitación y comparendos.

El objetivo es explorar si existen diferencias en la cantidad de accidentes y comparendos entre los días con lluvia y los días sin lluvia.

## Objetivo

Analizar la relación entre:

- Accidentes de tránsito.
- Precipitación registrada.
- Comparendos registrados.

El análisis se realiza utilizando Python, Pandas y Matplotlib.

## Conjuntos de datos

Para el proyecto se utilizaron tres conjuntos de datos:

### 1. Accidentalidad en Barranquilla

- **Fuente:** Datos Abiertos Colombia
- **Formato:** CSV
- **Registros:** 28.523
- **Columnas:** 11

Principales variables:

- `FECHA_ACCIDENTE`
- `HORA_ACCIDENTE`
- `GRAVEDAD_ACCIDENTE`
- `CLASE_ACCIDENTE`
- `SITIO_EXACTO_ACCIDENTE`
- `CANT_HERIDOS_EN _SITIO_ACCIDENTE`
- `CANT_MUERTOS_EN _SITIO_ACCIDENTE`
- `CANTIDAD_ACCIDENTES`
- `AÑO_ACCIDENTE`
- `MES_ACCIDENTE`
- `DIA_ACCIDENTE`

### 2. Precipitación en Barranquilla

- **Fuente:** IDEAM - Datos Abiertos Colombia
- **Formato:** CSV
- **Registros:** 50.000
- **Municipio:** Barranquilla

La variable principal es:

- `valorobservado`: precipitación registrada en milímetros (mm).

### 3. Comparendos en Barranquilla

- **Formato:** CSV
- **Registros:** 357.743
- **Columnas:** 9

Principales variables:

- `fecha_comparendo`
- `COD_INFRACCION`
- `DESC_INFRACCION`
- `TIPO_INFRACCION`
- `SERVICIO_VEHICULO_INFRACTOR`
- `CLASE_VEHICULO_INFRACTOR`
- `CANTIDAD_INFRACCIONES`
- `Tipo Camara`
- `Camara_y_direccion`

## Tecnologías utilizadas

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Visual Studio Code
- Git y GitHub

## Estructura del proyecto

```text
mineria-datos-accidentes-v2/
│
├── dataset/
│   ├── Accidentalidad_en_Barranquilla_20260830.csv
│   ├── precipitacion_barranquilla.csv
│   ├── Comparendos_Barranquilla.csv
│   ├── Accidentalidad_en_Barranquilla_limpio.csv
│   ├── precipitacion_barranquilla_limpio.csv
│   └── Comparendos_Barranquilla_limpio.csv
│
├── src/
│   ├── __init__.py
│   ├── accidentes.py
│   ├── precipitacion.py
│   ├── comparendos.py
│   └── integracion.py
│
├── analisis/
│   └── analisis_datos.ipynb
│
└── README.md