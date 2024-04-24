

class diccX:
    
    def __init__(self):
        def listaMinusculas(lista):
            listaM=[]
            for i in lista:
                listaM.append(i.lower())
        
            return listaM
        
        self._palabrasPositivas=listaMinusculas(["quiere","Xóchitl","quieree","mexico","contigo","cambio","presidenta","Gálvez","unidos"
                        ,"transparencia","capaz","vamos","XOCHITL","TODO","LINDA","reina","queremos","talento",
                        "iniciativas",
                        ])
        self._palabrasNegativas=listaMinusculas(["minimo","vengas","teleprompter","warzone","fuera","violento","lea","trabarse","nada"
                   ,"pobres", "cumplir","capacidad","entender","malo","Xorrupta","Inepta","Nefasta","vendida",
                   "Rata","Mentirosa","lacra","Cobarde","LameBotas","Intrigosa","Vergüenza","minimo"
                   "fraude","perder","ingles","hambre","sed","robado","vender","perdiendo","derrota","manipulen",
                   "empresarios","leyendo","discurso","sin","carbura","ardilla","ferrocarril","risa","chistosa",
                   "canuta","miedo","PANISTAS","CASTIGO","soñando","unde","títere","PRI","PAN","desilusióna"])
        
        
        self._otroPartido=listaMinusculas(["morena","amlo","Claudia","Sheinbaum","tren","Maya"])
        
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
         
    
        
    
    
    
    
       
  
    
    
     


