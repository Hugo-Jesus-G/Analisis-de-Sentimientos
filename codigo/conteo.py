class Conteos:
    
    def conteoPalabras(listaSentimientos,listaFiltrada,diccionario):
        for palabra in listaFiltrada:
            palabras=palabra.split();
            
            for sentimiento in palabras:
                
                if sentimiento in listaSentimientos:
                    if sentimiento not in diccionario:
                        diccionario[sentimiento] = 1
                    elif sentimiento in diccionario:
                        diccionario[sentimiento]+=1
    
        return diccionario
    
    
    
    
    def numeroPalabras(dicc):
        
        return sum(dicc.values())
        
        
        
    def numeroTotalPalabras(dicc1,dicc2):
        return dicc1+dicc2
    
    
    def porcentaje(dicc1,dicc2):
        return dicc1/(dicc1+dicc2)
        
        
        
    
        
        
        
        
    
        
        
        
    
  
     

        
        
        
        