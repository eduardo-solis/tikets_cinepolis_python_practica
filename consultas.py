from functools import total_ordering
import json
import datetime

class Consulta:

    def __init__(self, dia, mes, tipo_consulta):
        self.dia = dia
        self.mes = mes
        self.tipo_consulta = tipo_consulta

    def realizarConsulta(self):
        opcion = self.tipo_consulta
        
        if opcion == '0':
            return self.consultarVentasDia()
        else:
            return self.consultarVentasMes()

    def consultarVentasDia(self): # Parametro dia
        dia = self.dia
        lista_dias = []
        lista = []
        
        archivo = open('ventas.txt', 'r')
        
        for linea in archivo:
            linea = linea.rstrip()
            venta = json.loads(linea)
            lista.append(venta)
        
        archivo.close()
        
        for item in lista:
            
            aux = self.obtener_dia(item['fecha_venta'])
            
            if aux == dia:
                lista_dias.append(item)
        
        return lista_dias
    
    def consultarVentasMes(self): # Parametro mes
        mes = self.mes
        lista_mes = []
        lista = []
        
        archivo = open('ventas.txt', 'r')
        
        for linea in archivo:
            linea = linea.rstrip()
            venta = json.loads(linea)
            lista.append(venta)
        
        archivo.close()
        
        for item in lista:
            
            aux = self.obtener_mes(item['fecha_venta'])
            
            if aux == mes:
                lista_mes.append(item)
        
        return lista_mes
    
    def obtener_dia(self, fecha):
        
        numero_dia = int(fecha[8:])
        mes = int(fecha[5:7])
        anio = int(fecha[:4])
        
        x = datetime.datetime(anio, mes, numero_dia)
        
        day = x.strftime("%w")
        
        return day
    
    def obtener_mes(self, fecha):
        
        numero_dia = int(fecha[8:])
        mes = int(fecha[5:7])
        anio = int(fecha[:4])
        
        x = datetime.datetime(anio, mes, numero_dia)
        
        month = x.strftime("%m")
        
        return month
    
    def obtener_totalVentas(self, lista):
        
        total = 0
        
        if len(lista) == 0:
            return 0
        
        else:
            
            for item in lista:
                total += float(item['cantidad_pagar'])
            
            return round(total, 2)