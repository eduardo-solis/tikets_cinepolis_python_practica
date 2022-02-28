import json

class Venta:
    
    def __init__(self, compradores, tikets, descuento, fecha, cliente):
        self.compradores = compradores
        self.tikets = tikets
        self.descuento = descuento
        self.fecha = fecha
        self.cliente = cliente
    
    def realizarVenta(self):
        
        if self.validarVenta():
            descuento = self.obtenerDescuento()
            subtotal = self.tikets * 12
            cantidad_pagar = subtotal - (subtotal * descuento)
            
            nombre_archivo = 'ventas.txt'
            
            try:
                leer_archivo = open(nombre_archivo, 'r')
                id = len(leer_archivo.readlines()) + 1
                leer_archivo.close()
            except:
                id = 1
            
            escribir_archivo = open(nombre_archivo,'a')
            
            venta = {
                'id' : id,
                'nombre_cliente' : self.cliente,
                'cantidad_compradores' : self.compradores,
                'cantidad_tikets' : self.tikets,
                'cantidad_pagar' : cantidad_pagar,
                'fecha_venta' : str(self.fecha)
            }
            
            escribir_archivo.write(json.dumps(venta) + '\n')
            escribir_archivo.close()

            return str(cantidad_pagar)
        else:
            return 'No se pudo realizar la venta'
    
    
    def obtenerDescuento(self):
        
        descuento = self.descuento
        cantidad_tikets = self.tikets
        
        if descuento == '0':
            if cantidad_tikets > 5:
                return 0.15
            elif cantidad_tikets >= 3 and cantidad_tikets <= 5:
                return 0.1
            else:
                return 0
        else:
            if cantidad_tikets > 5:
                return 0.25
            elif cantidad_tikets >= 3 and cantidad_tikets <= 5:
                return 0.2
            else:
                return 0.1

    def validarVenta(self):
        
        cantidad_compradores = self.compradores
        cantidad_tikets = self.tikets
        
        aux = (cantidad_compradores * 7) - cantidad_tikets
        
        if aux > 0:
            return True
        else:
            return False
    