
import os
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto
from diccionariosX import diccX
from conteo import Conteos
from clasificador import clasificacion
from exportarExel import exportar

class mainX():
    
    def __init__(self,ruta,diccionario):
        self.porcentajePalabras={}
        self.porcentajeComentarios={}
        self.ruta=ruta
        self.diccionario=diccionario
        
    def getPorcentajePalabras(self):
        return self.porcentajePalabras
    
    def getPorcentajeComentarios(self):
        return self.porcentajeComentarios
        
        
    def limpiar(self):   
        

        lista=extraccion.extraccionColumnaComnetarios(self.ruta)
        #extraccion.mostrarComentariosExtraidos(lista)
        listaLimpia=limpiarTexto.limpiar(lista)
        #limpiarTexto.mostrarListaLimpia(listaLimpia)
        return listaLimpia
    
    def palabrasPorcentajes(self):

        #conteos
        diccP=Conteos.conteoPalabras(self.diccionario.getPalabrasPositivas(),self.limpiar(),self.diccionario.getdiccionarioParaConteoPositivos())
        print("\n\nconteo de palabras positivas\n")
        print(diccP)

        diccN=Conteos.conteoPalabras(self.diccionario.getPalabrasNegativas(),self.limpiar(),self.diccionario.getdiccionarioParaConteoNegativos())
        print("\n\nconteo de palabras Negativas\n")
        print(diccN)
        print("\n")
        numeroP=Conteos.numeroPalabras(diccP)
        numeroN=Conteos.numeroPalabras(diccN)
        total=Conteos.numeroTotalPalabras(numeroP,numeroN)
        porcentajeP=Conteos.porcentaje(numeroP,numeroN)
        porcentajeN=Conteos.porcentaje(numeroN,numeroP)
        print("El numero de palabras postivas es:"+str(numeroP))
        print("El numero de palabras Negativos es:"+str(numeroN))
        print("El numero de palabras Totales es:"+str(total))
        print("El porcentaje de palabras Positivas es:"+str(porcentajeP))
        print("El porcentaje de palabras Negativas es:"+str(porcentajeN))
        
        porcentajePalabras={
                "Positivas":porcentajeP,
                "Negativas":porcentajeN
            
            }
        
        return porcentajePalabras



    def clasificacionYExportacion(self,rutaArchivo):
        #clasificacion
        clasificacionn=clasificacion()
        clasificacionn.clasificar(self.limpiar(),self.diccionario.getPalabrasPositivas(),self.diccionario.getPalabrasNegativas())

        numeroComentarios=clasificacionn.numeroPorCategoria()
        numeroTotalComentarios=sum(numeroComentarios.values())
        print("\n\nEl numero de comentarios  es :"+str(numeroComentarios))
        print("El numero total de comentarios es:"+str(numeroTotalComentarios))

        porcentajeComentarios=clasificacionn.porcentajePorCategoria()
       

        print("\nLos porcentajes de la clasificacion de los comentarios es \n:"+str(porcentajeComentarios))
        print()
        print()
        
        exportar.exportarAExel(self.limpiar(),clasificacionn.getCoincidencias(),clasificacionn.getCategoria(),rutaArchivo,self.diccionario.getdiccionarioParaConteoPositivos(),self.diccionario.getdiccionarioParaConteoNegativos())
        
        
        return porcentajeComentarios
    
    
    
    
        
        
        
            
    
    


















