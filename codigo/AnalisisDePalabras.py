from conteo import Conteos
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto


class Analisis:
    
    def getextraccionComenatrios(ruta):
        return extraccion.extraccionColumnaComnetarios(ruta)
    
    def getListaLimpia(listaComentariosExtraidos):
        return limpiarTexto.limpiar(listaComentariosExtraidos)
    
    def getConteos(diccionarioSentimientos, listaLimpia, diccionario):
        return Conteos.conteoPalabras(diccionarioSentimientos, listaLimpia, diccionario)
    
    def analisisPalabras(ruta, diccionario, diccionarioSentimientos):
        # extraccion de comentarios 
        listaComentariosExtraidos = Analisis.getextraccionComenatrios(ruta)

        # limpiar lista
        listaLimpia = Analisis.getListaLimpia(listaComentariosExtraidos)

        return Analisis.getConteos(diccionarioSentimientos, listaLimpia, diccionario)
