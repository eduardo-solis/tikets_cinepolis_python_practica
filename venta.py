class Venta:
    
    def __init__(self, compradores, tikets, descuento):
        self.compradores = compradores
        self.tikets = tikets
        self.descuento = descuento
    
    def realizarVenta(self):
        
        if self.validarVenta():
            descuento = self.obtenerDescuento()
            subtotal = self.tikets * 12
            cantidad_pagar = subtotal - (subtotal * descuento)
            
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