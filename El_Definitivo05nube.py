import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 0: Elegir que base de datos según el número de la probeta 0.5 
# Probeta 1: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_1.csv 
# Probeta 2: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_2.csv 
# Probeta 3: https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_3.csv 

# Paso 1: Leer y procesar el archivo completo
df = pd.read_csv('https://raw.githubusercontent.com/Hetskuni/Materiales/main/DatosEnsayoProbeta05_1.csv', sep=';')

# Paso 2: Convertir los datos de las columnas 'Extensión' y 'Carga' a formato numérico
df['Extensión (mm)'] = df['Extensión (mm)'].str.replace(',', '.').astype(float)
df['Carga (N)'] = df['Carga (N)'].str.replace(',', '.').astype(float)

# Paso 3: Calcular esfuerzo y deformación usando el área de sección transversal correcta
# Área transversal de la espuma en mm²
area_seccion = 2.5 * 2.5  # mm²

# Esfuerzo = Carga / Área (en MPa)
df['Esfuerzo (MPa)'] = df['Carga (N)'] / area_seccion / 1e6  # Convertir a MPa

# Deformación = Extensión / Longitud original (suponiendo longitud original conocida)
longitud_original = 50.0  # Modificar según la longitud original de la probeta en mm
df['Deformación (mm/mm)'] = df['Extensión (mm)'] / longitud_original

# Paso 4: Calcular la tenacidad (área bajo la curva esfuerzo-deformación)
tenacidad = np.trapz(df['Esfuerzo (MPa)'], df['Deformación (mm/mm)'])
print(f"Tenacidad calculada: {tenacidad:.4f} MPa")

# Paso 5: Graficar la curva esfuerzo-deformación
plt.figure(figsize=(10, 6))
plt.plot(df['Deformación (mm/mm)'], df['Esfuerzo (MPa)'], 'b-', alpha=0.75)
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Curva Esfuerzo-Deformación')
plt.grid(True)
plt.show()
