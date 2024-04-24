from main import Main
from diccionariosC import diccC
from conteo import Conteos
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto
from crearGrafica import grafica
import os

ruta_actual = os.getcwd()
ruta=ruta_actual+'\\datosC\\General.xlsx'

diccc=diccC()
        

diccc.setdiccionarioParaConteoPositivos(Main.analisisPalabras(ruta,diccc.getdiccionarioParaConteoPositivos(),diccc.getPalabrasPositivas()))

print(f"\n-----------------Conteo de Palabras Positivas---------------\n \n{diccc.getdiccionarioParaConteoPositivos()}")








##conteo de palabras Negativas




diccc.setdiccionarioParaConteoNegativos(Main.analisisPalabras(ruta,diccc.getdiccionarioParaConteoNegativos(),diccc.getPalabrasNegativas()))

print(f"\n-----------------Conteo de Palabras Negativas---------------\n \n{diccc.getdiccionarioParaConteoNegativos()}")



palabrasPositivas=sum(diccc.getdiccionarioParaConteoPositivos().values())
palabrasNegativas=sum(diccc.getdiccionarioParaConteoNegativos().values())
print("EL numero de palabras POSITIVAS es:"+str(palabrasPositivas))

print("EL numero de palabras Negativas es:"+str(palabrasNegativas))
print("palabras totales",str(palabrasNegativas+palabrasPositivas))

print("Porcentaje de palabras Positivas:",str(palabrasPositivas/(palabrasPositivas+palabrasNegativas)))
print("Porcentaje de palabras Negativas:",str(palabrasNegativas/(palabrasPositivas+palabrasNegativas)))
        
porcentajes={
    "Positivo":palabrasPositivas/(palabrasPositivas+palabrasNegativas),
    "Negativo":palabrasNegativas/(palabrasPositivas+palabrasNegativas)
    
}   
grafica.crearGraficoCircular(porcentajes.keys(),porcentajes.values())
