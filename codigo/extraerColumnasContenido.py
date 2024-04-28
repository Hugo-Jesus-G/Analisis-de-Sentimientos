import pandas as pd


class extraccion:
    listaComentarios=[]

    def extraccionColumnaComnetarios(ruta):
        documento = pd.read_excel(ruta)

        columna = documento['Comentario']
        listaComentarios = columna.tolist()
            
        return listaComentarios
    
    
    def mostrarComentariosExtraidos(lista):
        print("\n-------------Comentarios Extraidos----------------")
        for i in lista :
            print(i,end='\n')







