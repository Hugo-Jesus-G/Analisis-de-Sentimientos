from clasificador import clasificacion
from exportarExel import exportar
from crearGrafica import grafica
from AnalisisDePalabras import Analisis
from diccionariosX import diccX
from conteo import Conteos
from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto
import os

class mainC():
    def __init__(self, rutaActual, diccionario):
        self.ruta = rutaActual
        self.dicc = diccionario
       
        
    def conteoPalabrasPositivas(self):
        self.dicc.setdiccionarioParaConteoPositivos(Analisis.analisisPalabras(self.ruta,self.dicc.getdiccionarioParaConteoPositivos(),self.dicc.getPalabrasPositivas()))
        return self.dicc.getdiccionarioParaConteoPositivos()
    
    def conteoPalabrasNegativas(self):
         self.dicc.setdiccionarioParaConteoNegativos(Analisis.analisisPalabras(self.ruta,self.dicc.getdiccionarioParaConteoNegativos(),self.dicc.getPalabrasNegativas()))
         return self.dicc.getdiccionarioParaConteoNegativos()
    
    def sumaPalabras(self,diccionario):
        return sum(diccionario.values())
   
    def sumaPalabrasTotales(self,numero1, numero2):
        return numero1 + numero2
    
    def calcularPorcentajes(self,numero1, numero2):
        return numero1 / (numero1 + numero2)
    
        
    def porcentajePalabras(self):
        #conteo de palabras positivas
        frecuenciaPositivo =dict()
        frecuenciaPositivo=self.conteoPalabrasPositivas()
        self.dicc
        print(f"\n-----------------Conteo de Palabras Positivas---------------\n \n"+str(frecuenciaPositivo))
        
        ##conteo de palabras Negativas
        frecuenciaNegativa =dict()
        frecuenciaNegativa= self.conteoPalabrasNegativas()
        print(f"\n-----------------Conteo de Palabras Negativas---------------\n \nself"+str(frecuenciaNegativa))

        ##numero de palabras
        palabrasPositivas = self.sumaPalabras(frecuenciaPositivo)
        palabrasNegativas = self.sumaPalabras(frecuenciaNegativa)

        print("EL numero de palabras POSITIVAS es:"+str(palabrasPositivas))
        print("EL numero de palabras Negativas es:"+str(palabrasNegativas))
        
        palabrasTotales = self.sumaPalabrasTotales(palabrasPositivas, palabrasNegativas)
        print("palabras totales",str(palabrasTotales))

        porcentajePositivo = self.calcularPorcentajes(palabrasPositivas, palabrasTotales)
        print("Porcentaje de palabras Positivas:",str(porcentajePositivo))
        
        porcentajeNegativo = self.calcularPorcentajes(palabrasNegativas, palabrasTotales)
        print("Porcentaje de palabras Negativas:",str(porcentajeNegativo))

        porcentajes={
            "Positivo": porcentajePositivo,
            "Negativo": porcentajeNegativo
        }   
        
        
        
        return porcentajes
    
    
    
    
    def porcentajeComentarios(self,rutaArchivo):
        clasificar=clasificacion(self.ruta)
        clasificar.clasificar(self.dicc.getPalabrasPositivas(),self.dicc.getPalabrasNegativas())
    

        exportar.exportarAExel(clasificar.getListaLimpia(),clasificar.getCoincidencias(),clasificar.getOrigenCoincidencias(),rutaArchivo,self.dicc.getdiccionarioParaConteoNegativos(),self.dicc.getdiccionarioParaConteoPositivos())
        
      
        return clasificar.numeroPorCategoria()
    
    