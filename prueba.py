import pandas as pd

tabla=pd.read_csv('./Siembras.csv')

#tabla estadisticas
tablaEstadisticas=tabla.describe()

#solo obtener medias de la tabla estadistica (solo 1 fila)
tablaMedias=tablaEstadisticas.loc[['mean']]

#solo obtener los datos de una columna
tablaMediaArboles=tablaMedias["Arboles"].to_frame()