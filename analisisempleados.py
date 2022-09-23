import pandas as pd

tablaEmpleados = pd.read_csv('./empleados.csv')
#para imprimir solo los primeros y ultimos 5 datos de la tabla
#print(tablaEmpleados) 
#para imprimir todos los datos de la tabla
#print(tablaEmpleados.to_string()) 
#filtro 1 deseo obtener todos los datos de los analistas 1
tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
archivoHTML=tablaAnalistas1.to_html()
archivoTEXTO=open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalistas1.to_html()
archivoTEXTO=open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()