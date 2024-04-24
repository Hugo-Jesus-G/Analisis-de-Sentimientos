from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

import matplotlib.pyplot as plt

class grafica:
    #grafica  de barras en exel
    '''
    def crearGrafica(data,nombre):
        wb = Workbook()
        ws = wb.active
        for row in data:
            ws.append(row)

        chart = BarChart()
        chart.add_data(Reference(ws, min_col=2, min_row=1, max_row=len(data), max_col=len(data)))
        chart.set_categories(Reference(ws, min_col=1, min_row=1, max_row=len(data)))
        ws.add_chart(chart, "E3")

        
        wb.save(nombre+".xlsx")


'''
#grafica con matploit
    def crearGraficoBarras(clave,valor):
        plt.bar(clave,valor)
        plt.show()
        
    def crearGraficoCircular(clave,valor):
        plt.pie(valor,labels=clave,autopct='%1.1f%%')
        plt.show()
        
        
        






