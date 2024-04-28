

class diccX:
     
    def __init__(self):   
        self._palabrasPositivas=["quiere","Xóchitl","quieree","mexico","contigo","cambio","presidenta","Gálvez","unidos"
                        ,"transparencia","capaz","vamos","XOCHITL","TODO","LINDA","reina","queremos","talento",
                        "iniciativas",
                        ]
        self._palabrasNegativas=["minimo","vengas","teleprompter","warzone","fuera","violento","lea","trabarse","nada"
                   ,"pobres", "cumplir","capacidad","entender","malo","Xorrupta","Inepta","Nefasta","vendida",
                   "Rata","Mentirosa","lacra","Cobarde","LameBotas","Intrigosa","Vergüenza","minimo"
                   "fraude","perder","ingles","hambre","sed","robado","vender","perdiendo","derrota","manipulen",
                   "empresarios","leyendo","discurso","sin","carbura","ardilla","ferrocarril","risa","chistosa",
                   "canuta","miedo","PANISTAS","CASTIGO","soñando","unde","títere","PRI","PAN","desilusióna","retiene"]
        
        
        self._otroPartido=["morena","amlo","Claudia","Sheinbaum","tren","Maya"]
        
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
         
    
        
    
    
    
    
       
  
    
    
     


