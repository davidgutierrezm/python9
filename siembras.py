import pandas as pd

tablaSiembras = pd.read_csv('./Siembras.csv')
#print(tablaSiembras) 
#tablaMunicipios1=tablaSiembras[tablaSiembras["Ciudad"]=="Andes"].head(50)
#archivoHTML=tablaMunicipios1.to_html()
#archivoTEXTO=open("datosandes.html","w")
#archivoTEXTO.write(archivoHTML)
#archivoTEXTO.close()
tablaMunicipios2=tablaSiembras[tablaSiembras["Ciudad"]=="Barbosa"].head(50)
archivoHTML=tablaMunicipios2.to_html()
archivoTEXTO=open("datosbarbosa.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()