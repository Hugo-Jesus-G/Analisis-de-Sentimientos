from extraerColumnasContenido import extraccion
from limpieza import limpiarTexto


class clasificacion:
    def __init__(self) :
        self.coincidencias = []
        self.categoria = []
       
        
    
    def getCoincidencias(self):
        return self.coincidencias

    def getCategoria(self):
        return self.categoria
    
    
    def clasificar(self,listaLimpia,diccionarioPositivo,diccionarioNegativo):
            for comentario in listaLimpia:
             
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

                                
                        
                self.categoria.append(clasificacion)
        
        
        

       
            
            
    def numeroPorCategoria(self):
        conteo = {
        "Positivo": sum(lista.count("Positivo") for lista in self.categoria),
        "Negativo": sum(lista.count("Negativo") for lista in self.categoria),
        "Neutral": sum(lista.count("Neutral") for lista in self.categoria)
        }
        return conteo
    
    def porcentajePorCategoria(self):
        conteo = self.numeroPorCategoria()
        totalElementos = sum(conteo.values())
        
        porcentajes = {}
        for categoria, cantidad in conteo.items():
            porcentaje = (cantidad / totalElementos) 
            porcentajes[categoria] = porcentaje
        
        return porcentajes

        