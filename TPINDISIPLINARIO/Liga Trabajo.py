import pandas as pd

df = pd.read_csv("FutbolLiga.csv")

ff = pd.read_csv("UltimaFecha.csv")

print("Tabla completa:")
print(df.head(10))
print("-" * 83)

print("Fecha Final:")
print(ff.head(10))
print("-" * 116)

print(df.info())

print(ff.info())

#Dia -> Objet. Pasar a int

ff['Dia'] = ff['Dia'].str.replace(' de Diciembre', '.12').astype(float) 

print(ff.head(10))
print(ff.info())

ff['Goleadores'] = ff['Goleadores'].fillna('No hubo gol')

print(ff.head(10))

