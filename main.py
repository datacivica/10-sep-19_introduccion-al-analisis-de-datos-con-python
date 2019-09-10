# 10/sep/19 - Introducción al Análisis de Datos con Python

"""
Impresión en consola
"""

print("# Impresión en consola")

print(4)

"""
Operadores
"""

print("# Operadores")

# Suma
print(2+2)

# Resta
print(5-4)

# Multiplicación
print(4*2)

# Potencia
print(2**3)

# División
print(10/5)

# Módulo
print(8 % 5)

# Mayor que
print(1 > 4)

# Menos que
print(4 > 1)

"""
Tipos de datos
"""

print("# Tipos de datos")

# Entero
print(5)

# Flotante
print(5.23847)

# Texto
print("Data Cívica")

# Lista
print(["Jorge","Pedro","Luis","Juan"])

# Diccionario
print({
  "Nombre":"Jorge",
  "Email":"jorandradefig@gmail.com"
  })

"""
Variables (Objetos)
"""

# Almacenar datos en una variable
nombres = ["Jorge","Pedro","Luis","Juan"]
print(nombres)

"""
Bibliotecas
"""

# Importar una biblioteca
import pandas as pd

"""
Lectura de bases de datos
"""

# Leer una base de datos
desaparecidos = pd.read_csv("rnped_fuerocomun_31_07_17_2.csv")

print(desaparecidos)

# Tipo de dato de la base de datos
print(type(desaparecidos))

# Primeras observaciones de la base de datos
print(desaparecidos.head())

# Últimas observaciones de la base de datos
print(desaparecidos.tail())

# Dimensiones de la base de datos
print(desaparecidos.shape)

# Columnas de la base de datos
print(desaparecidos.columns)

# Tipos de datos de las columnas de la base de datos
print(desaparecidos.dtypes)

"""
Procesamiento de bases de datos
"""

# Seleccionar una columna
print(desaparecidos['fuerocomun_edad'])

# Seleccionar los valores únicos de una columna
print(pd.unique(desaparecidos['fuerocomun_edad']))

# Estadísticas descriptivas
print(desaparecidos['fuerocomun_edad'].describe())
