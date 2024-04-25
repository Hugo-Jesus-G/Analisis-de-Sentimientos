from conteo import Conteos
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto


class Analisis:
    
    
    def analisisPalabras(ruta,diccionario,diccionarioSentimientos):
        
        

        #extraccion de comentarios 
        listaComentariosExtraidos=extraccion.extraccionColumnaComnetarios(ruta)

       # extraccion.mostrarComentariosExtraidos(listaComentariosExtraidos)


        #limpiar lista

        listaLimpia = limpiarTexto.limpiar(listaComentariosExtraidos)

        #mostrar lista limpia
        #limpiarTexto.mostrarListaLimpia(listaLimpia)
        
       
        return Conteos.conteoPalabras(diccionarioSentimientos,listaLimpia,diccionario)
        


    