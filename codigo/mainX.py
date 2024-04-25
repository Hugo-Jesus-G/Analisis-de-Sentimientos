from crearGrafica import grafica
from AnalisisDePalabras import Analisis
from diccionariosX import diccX
from conteo import Conteos
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto
import os

ruta_actual = os.getcwd()
ruta=ruta_actual+'\\datosx\\General.xlsx'

diccx=diccX()
        


#conteo de palabras positivas
diccx.setdiccionarioParaConteoPositivos(Analisis.analisisPalabras(ruta,diccx.getdiccionarioParaConteoPositivos(),diccx.getPalabrasPositivas()))

print(f"\n-----------------Conteo de Palabras Positivas---------------\n \n{diccx.getdiccionarioParaConteoPositivos()}")








##conteo de palabras Negativas



diccx.setdiccionarioParaConteoNegativos(Analisis.analisisPalabras(ruta,diccx.getdiccionarioParaConteoNegativos(),diccx.getPalabrasNegativas()))

print(f"\n-----------------Conteo de Palabras Negativas---------------\n \n{diccx.getdiccionarioParaConteoNegativos()}")

palabrasPositivas=sum(diccx.getdiccionarioParaConteoPositivos().values())
palabrasNegativas=sum(diccx.getdiccionarioParaConteoNegativos().values())

print("EL numero de palabras POSITIVAS es:"+str(palabrasPositivas))

print("EL numero de palabras Negativas es:"+str(palabrasNegativas))
print("palabras totales",str(palabrasNegativas+palabrasPositivas))

print("Porcentaje de palabras Positivas:",str(palabrasPositivas/(palabrasPositivas+palabrasNegativas)))
print("Porcentaje de palabras Negativas:",str(palabrasNegativas/(palabrasPositivas+palabrasNegativas)))

porcentajes={
    "Positivo":palabrasPositivas/(palabrasPositivas+palabrasNegativas),
    "Negativo":palabrasNegativas/(palabrasPositivas+palabrasNegativas)
    
}   



'''grafica.crearGrafica(diccx.getdiccionarioParaConteoPositivos().items(),"PositivosX")
grafica.crearGrafica(diccx.getdiccionarioParaConteoNegativos().items(),"NegativosX")
'''
'''grafica.crearGraficoCircular(diccx.getdiccionarioParaConteoNegativos().keys(),diccx.getdiccionarioParaConteoNegativos().values())
'''

grafica.crearGraficoCircular(porcentajes.keys(),porcentajes.values())

        
        
    
    
