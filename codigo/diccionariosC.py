

class diccC:
    
    def __init__(self):
        def listaMinusculas(lista):
            listaM=[]
            for i in lista:
                listaM.append(i.lower())
        
            return listaM
        
        self._palabrasPositivas=listaMinusculas(["mejor","presidenta","Claudia","sheinbaum","morena","arriba","transformado","viva",
                    "contigo","vamos","primera","honor","ganar","carismática","bien","patrona","soporten",
                    "amlo","futura","determinado","masivo","voto","best","mexico"])
        self._palabrasNegativas=listaMinusculas(["acarreados","malo","descuidara","cansado","destrucción","mafia","nunca","bad"])
        
        
        self._otroPartido=listaMinusculas(["Xóchitl"])
        
        self._diccionarioParaConteoPositivos=dict()
        self._diccionarioParaConteoNegativos=dict()
    
    

    def getPalabrasPositivas(self):
        return self._palabrasPositivas
    
    def getPalabrasNegativas(self):
        return self._palabrasNegativas 
    
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
         
    
        
    
    
    
    
       
  
    
    
     



    
    



