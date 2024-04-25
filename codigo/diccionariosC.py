

class diccC:
    
    def __init__(self):
        
        self._palabrasPositivas=["mejor","presidenta","Claudia","sheinbaum","morena","arriba","transformado","viva",
                    "contigo","vamos","primera","honor","ganar","carismática","bien","patrona","soporten",
                    "amlo","futura","determinado","masivo","voto","best","mexico"]
        
        self._palabrasNegativas=["acarreados","malo","descuidara","cansado","destrucción","mafia","nunca","bad"]
        
        
        self._otroPartido=["Xóchitl"]
        
        self._diccionarioParaConteoPositivos=dict()
        self._diccionarioParaConteoNegativos=dict()
    
    
    def listaMinusculas(self,lista):
        return {palabra.lower() for palabra in lista}

    def getPalabrasPositivas(self):
        return self.listaMinusculas(self._palabrasPositivas)
    
    def getPalabrasNegativas(self):
        return self.listaMinusculas(self._palabrasNegativas)
    
    def getPalabrasOtroPartido(self):
        return self._otroPartido 

     #alamcenamineto de conteo positivos

    def getdiccionarioParaConteoPositivos(self):
        return self._diccionarioParaConteoPositivos
    
    def setdiccionarioParaConteoPositivos(self,actualizacion):
         self._diccionarioParaConteoPositivos.update(actualizacion)
         
    #alamcenamineto de conteo negativos
    def getdiccionarioParaConteoNegativos(self):
        return self._diccionarioParaConteoNegativos
    
    def setdiccionarioParaConteoNegativos(self,actualizacion):
         self._diccionarioParaConteoNegativos.update(actualizacion)
         
    
        
    
    
    
    
       
  
    
    
     



    
    



