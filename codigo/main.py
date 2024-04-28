import os
from diccionariosC import diccC
from mainC import mainC
from mainX import mainX
from crearGrafica import grafica
from diccionariosX import diccX
from limpieza import limpiarTexto
from extraerColumnasContenido import extraccion
from exportarExel import exportar
from AnalisisDePalabras import Analisis
from clasificador import clasificacion


print("\n---------------------Xochitl------------")

diccionarioX=diccX()


rutaX=os.getcwd()+'\\datosx\\General.xlsx'
rutaArchivo=os.getcwd()+'\\datosx\\salidaAnalisisX.xlsx'
candidatoX=mainX(rutaX,diccionarioX)

porcentajePalabrasX=candidatoX.porcentajePalabras()

porcentajeComentariosX=candidatoX.porcentajeComnetarios(rutaArchivo)

print(porcentajeComentariosX)




#claudia

print("\n---------------------Claudia------------")
diccionarioC=diccC()


rutaC=os.getcwd()+'\\datosC\\General.xlsx'
rutaArchivo=os.getcwd()+'\\datosC\\salidaAnalisisC.xlsx'
candidatoC=mainC(rutaC,diccionarioC)

porcentajePalabrasC=candidatoC.porcentajePalabras()

porcentajeComentariosC=candidatoC.porcentajeComentarios(rutaArchivo)

print(porcentajeComentariosC)
#el primero parametro es de claudia y el segundo de xochitl
grafica.crearGraficosCircularesComparacion(porcentajeComentariosC,porcentajeComentariosX)


