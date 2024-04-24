from crearGrafica import grafica
from main import Main
from diccionariosX import diccX
from conteo import Conteos
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto





diccx=diccX()
        
ruta='~\\OneDrive\\Documentos\\semestres\\SeptimoSemestre\\mineriaDatos\\Proyecto\\Analisis-de-Sentimientos\\datosC\\General.xlsx'

#conteo de palabras positivas
diccx.setdiccionarioParaConteoPositivos(Main.analisisPalabras(ruta,diccx.getdiccionarioParaConteoPositivos(),diccx.getPalabrasPositivas()))

print(f"\n-----------------Conteo de Palabras Positivas---------------\n \n{diccx.getdiccionarioParaConteoPositivos()}")








##conteo de palabras Negativas



diccx.setdiccionarioParaConteoNegativos(Main.analisisPalabras(ruta,diccx.getdiccionarioParaConteoNegativos(),diccx.getPalabrasNegativas()))

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

        
        
    
    
