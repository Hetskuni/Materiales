import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Paso 0: Elegir el número de la probeta
numero_probeta = input("Ingrese el número de la probeta (1, 2, o 3): ")

# Validar la entrada y asignar el archivo correspondiente
if numero_probeta == '1':
    archivo_csv = 'DatosEnsayoProbeta05_1.csv'
elif numero_probeta == '2':
    archivo_csv = 'DatosEnsayoProbeta05_2.csv'
elif numero_probeta == '3':
    archivo_csv = 'DatosEnsayoProbeta05_3.csv'
else:
    print("Número de probeta inválido. Intente nuevamente.")
    exit()

# Paso 1: Leer y procesar el archivo completo
df = pd.read_csv(archivo_csv, sep=';')

# Paso 2: Convertir los datos de las columnas 'Extensión' y 'Carga' a formato numérico
df['Extensión (mm)'] = df['Extensión (mm)'].str.replace(',', '.').astype(float)
df['Carga (N)'] = df['Carga (N)'].str.replace(',', '.').astype(float)

# Paso 3: Calcular esfuerzo y deformación (asumiendo área de sección transversal constante y conocida)
area_seccion = 2.5 * 2.5  # Área de la sección transversal de la probeta en mm²

# Esfuerzo = Carga / Área
df['Esfuerzo (MPa)'] = df['Carga (N)'] / area_seccion / 1e6  # Convertir a MPa

# Deformación = Extensión / Longitud original (modificar según la longitud original de la probeta)
longitud_original = 50.0  # Longitud original de la probeta en mm (modificar si es necesario)
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
