from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

import matplotlib.pyplot as plt

class grafica:
   
#grafica con matploit
    def crearGraficoBarras(clave,valor):
        plt.bar(clave,valor)
        plt.show()
        
    def crearGraficoCircular(clave,valor):
        plt.pie(valor,labels=clave,autopct='%1.1f%%')
        plt.show()
        

    def crearGraficosCircularesComparacion(candidato1, candidato2,tipo):
    
        fig, axs = plt.subplots(1, 2)
        
        axs[0].pie(candidato1.values(), labels=candidato1.keys(), autopct='%1.1f%%')
        axs[0].set_title('Claudia')
        
        axs[1].pie(candidato2.values(), labels=candidato2.keys(), autopct='%1.1f%%')
        axs[1].set_title('Xochitl')
        fig.suptitle(f'Comparación de {tipo}')  # Título general
        plt.show()
        
        
        
    def crearGraficoCircular(clave,valor):
        plt.pie(valor,labels=clave,autopct='%1.1f%%')
        plt.show()
            
        






