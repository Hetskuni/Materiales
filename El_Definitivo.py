import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 0: Elegir que base de datos segun el numero de la probeta
# Probeta 1: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta_1.csv
# Probeta 2: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta_2.csv
# Probeta 3: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta_3.csv
# Probeta 4: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta_4.csv

# Paso 1: Leer y procesar el archivo completo
df = pd.read_csv('https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta_3.csv', sep=';')
df = df.drop(index=df.index[0])

# Convertir a numérico y eliminar filas no numéricas
columnas = ['Deformación por compresión', 'Esfuerzo de compresión']

# Reemplazar comas por puntos en las columnas especificadas
df[columnas] = df[columnas].replace({',': '.'}, regex=True)
df[columnas] = df[columnas].apply(pd.to_numeric)

# Calcular la tenacidad
tenacidad = np.trapz(df['Esfuerzo de compresión'], df['Deformación por compresión'])
print(f"Tenacidad calculada: {tenacidad:.10f} MPa")

print("\nPrimeras 5 filas del DataFrame procesado:")
print(df.head())
print("\nÚltimas 5 filas del DataFrame procesado:")
print(df.tail())


# Graficar una muestra de los datos
plt.figure(figsize=(10, 6))
sample_size = min(1000, len(df))
df_sample = df.sample(n=sample_size)
plt.plot(df_sample['Deformación por compresión'], df_sample['Esfuerzo de compresión'], 'b.', alpha=0.5)
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Muestra de la Curva Esfuerzo-Deformación')
plt.grid(True)
plt.show()
