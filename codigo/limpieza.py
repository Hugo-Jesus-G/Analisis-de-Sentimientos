import re
class limpiarTexto:
    
    
    def limpiar(lista):
        listaFiltrada = []
        for i in lista:
            palabras = i.split()
            palabrasFiltradas = []  
            
            for palabra in palabras:
                if 3 < len(palabra) <= 10:
                    
                    palabrasFiltradas.append(limpiarTexto.eliminarEmojis(palabra))
                
            cadenaLimpia = " ".join(palabrasFiltradas)
            listaFiltrada.append(cadenaLimpia.lower())  
        
        return listaFiltrada

    
    
    
    def mostrarListaLimpia(lista):
            print("\n-------------Comentarios Filtrados----------------")

            for i in lista :
                print(i,end='\n')     
    

    def eliminarEmojis(palabra):
        
        variantes = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # símbolos y pictogramas
                                u"\U0001F680-\U0001F6FF"  # transporte y símbolos de mapa
                                u"\U0001F1E0-\U0001F1FF"  # banderas (iOS)
                                u"\U0001F923"              # emoji  🤣
                                u"\U00002764"               #emoji  ❤️
                                u"\U0001F970"                 #emoji 🥰️
                                "]+", flags=re.UNICODE)
        
        # Eliminar emojis de la palabra
        palabraSinEmojis = variantes.sub(r'', palabra)
        
        return palabraSinEmojis
        
