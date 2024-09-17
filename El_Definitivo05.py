import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 0: Elegir que base de datos segun el numero de la probeta 0.5 
# Probeta 1: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_1.csv 
# Probeta 2: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_2.csv 
# Probeta 3: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_3.csv 

# Paso 1: Leer y procesar el archivo
url = 'https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_1.csv'
df = pd.read_csv(url, sep=';', decimal=',', thousands='.')

# Asegurarse de que las columnas tengan los nombres correctos
df.columns = ['Extensión (mm)', 'Carga (N)']

# Convertir a numérico y eliminar filas no numéricas
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()

# Calcular la tenacidad (área bajo la curva de carga vs. extensión)
# Usamos el valor absoluto para manejar valores negativos
tenacidad = np.trapz(np.abs(df['Carga (N)']), np.abs(df['Extensión (mm)']))
print(f"Tenacidad calculada: {tenacidad:.10f} N·mm")

print("\nPrimeras 5 filas del DataFrame procesado:")
print(df.head())
print("\nÚltimas 5 filas del DataFrame procesado:")
print(df.tail())

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(df['Extensión (mm)'], df['Carga (N)'], 'b-')
plt.xlabel('Extensión (mm)')
plt.ylabel('Carga (N)')
plt.title('Curva Carga-Extensión')
plt.grid(True)
plt.show()

# Calcular y mostrar estadísticas básicas
print("\nEstadísticas básicas:")
print(df.describe())

# Identificar puntos de interés
max_carga = df['Carga (N)'].abs().max()
max_extension = df['Extensión (mm)'].abs().max()
print(f"\nCarga máxima (absoluta): {max_carga:.2f} N")
print(f"Extensión máxima (absoluta): {max_extension:.5f} mm")