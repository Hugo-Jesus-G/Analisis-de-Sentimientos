import os
from diccionariosC import diccC
from mainC import mainC
from mainX import mainX
from crearGrafica import grafica
from diccionariosX import diccX
from limpieza import limpiarTexto
from extraerColumnasContenido import extraccion
from exportarExel import exportar
from clasificador import clasificacion


print("\n---------------------Xochitl------------")

rutaX=os.getcwd()+'\\datosx\\GeneralPostX.xlsx'
diccionarioX=diccX()

x=mainX(rutaX,diccionarioX)
x.limpiar()
porcentajePalabrasX=x.palabrasPorcentajes()

rutaGuardarX=os.getcwd()+'\\datosx\\analisisPostX.xlsx'

porcentajeComentariosX=x.clasificacionYExportacion(rutaGuardarX)

print("PALABRAS "+str(porcentajePalabrasX))
print("COMENTARIOS "+str(porcentajeComentariosX))



#claudia

print("\n---------------------Claudia------------")
rutaC=os.getcwd()+'\\datosC\\GeneralPostC.xlsx'
diccionarioC=diccC()

c=mainC(rutaC,diccionarioC)
c.limpiar()
porcentajePalabrasC=c.palabrasPorcentajes()

rutaGuardarC=os.getcwd()+'\\datosC\\analisisPostC.xlsx'

porcentajeComentariosC=c.clasificacionYExportacion(rutaGuardarC)

print("PALABRAS "+str(porcentajePalabrasC))
print("COMENTARIOS "+str(porcentajeComentariosC))





#graficas
#el primero parametro es de claudia y el segundo de xochitl
grafica.crearGraficosCircularesComparacion(porcentajeComentariosC,porcentajeComentariosX,"Comentarios")
#grafica.crearGraficosCircularesComparacion(porcentajePalabrasC,porcentajePalabrasX,"Palabras")



