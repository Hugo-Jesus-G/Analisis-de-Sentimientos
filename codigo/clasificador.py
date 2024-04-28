from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto


class clasificacion:
    def __init__(self,ruta) :
        self.ruta=ruta
        self.coincidencias = []
        self.origenCoincidencias = []
        self.listaLimpia = []
        
    
    def getCoincidencias(self):
        return self.coincidencias

    def getOrigenCoincidencias(self):
        return self.origenCoincidencias
    def getListaLimpia(self):
        return self.listaLimpia
    
    
    def clasificar(self,diccionarioPositivo,diccionarioNegativo):
        lista=extraccion.extraccionColumnaComnetarios(self.ruta)
        self.listaLimpia=limpiarTexto.limpiar(lista)
        
        coincidencias = []
        origenCoincidencias = []


        for comentario in self.listaLimpia:
             if comentario:
                coincidenciasComentario = [palabra for palabra in diccionarioNegativo if palabra.lower() in comentario.lower()] + \
                                        [palabra for palabra in diccionarioPositivo if palabra.lower() in comentario.lower()]
                self.coincidencias.append(coincidenciasComentario)
                
                clasificacion = []
            
                
                if coincidenciasComentario : 
                    if coincidenciasComentario[0] in diccionarioNegativo:
                            clasificacion.append("Negativo")
                    elif coincidenciasComentario[0] in diccionarioPositivo:
                            clasificacion.append("Positivo")
                else:
                    clasificacion.append("Neutral")

                                
                        
                self.origenCoincidencias.append(clasificacion)

       
            
            
    def numeroPorCategoria(self):
        conteo = {
        "positivo": sum(lista.count("Positivo") for lista in self.origenCoincidencias),
        "negativo": sum(lista.count("Negativo") for lista in self.origenCoincidencias),
        "neutral": sum(lista.count("Neutral") for lista in self.origenCoincidencias)
        }
        return conteo
    
    def porcentajePorCategoria(self):
        conteo = self.numeroPorCategoria()
        total_elementos = sum(conteo.values())
        
        porcentajes = {}
        for categoria, cantidad in conteo.items():
            porcentaje = (cantidad / total_elementos) 
            porcentajes[categoria] = porcentaje
        
        return porcentajes

        