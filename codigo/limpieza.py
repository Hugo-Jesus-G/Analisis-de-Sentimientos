
class limpiarTexto:
    
    
    def limpiar(lista):
        listaFiltrada = []
        for i in lista:
            palabras = i.split()
            palabrasFiltradas = []  
            
            for palabra in palabras:
                if 3 < len(palabra) <= 10:
                    palabrasFiltradas.append(palabra)
                
            cadenaLimpia = " ".join(palabrasFiltradas)
            listaFiltrada.append(cadenaLimpia.lower())  
        
        return listaFiltrada

    
    
    
    def mostrarListaLimpia(lista):
            print("\n-------------Comentarios Filtrados----------------")

            for i in lista :
                print(i,end='\n')        
        
