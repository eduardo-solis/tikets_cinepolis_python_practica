from flask import Flask, render_template, request

# Libreria de protección
from flask_wtf import CSRFProtect
# Libreria para mensajes flash
from flask import flash

import forms
import venta


app = Flask(__name__)

# Creación de la protección
app.secret_key = 'clave_secreta'
csrf = CSRFProtect(app)

@app.errorhandler(code_or_exception=404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route('/', methods=['GET', 'POST'])
def index():
    
    venta_form = forms.VentaForm(request.form)
    pago_venta = ''
    
    if request.method == 'POST' and venta_form.validate():
        
        compradores = venta_form.cantidad_compradores.data
        tikets = venta_form.cantidad_tikets.data
        tarjeta = venta_form.tarjeta_descuento.data
        
        venta_class = venta.Venta(compradores, tikets, tarjeta)
        
        pago_venta = venta_class.realizarVenta()
        
        # Creación del mensaje flash
        mensaje = ''
        if pago_venta.lower() == 'no se pudo realizar la venta':
            mensaje = 'No se pudo realizar la venta debio a que solo se puede comprar 7 tikets por persona'
        else:
            mensaje = 'Venta realizada exitosamente'
        
        flash(mensaje)
    
    return render_template('venta.html', form = venta_form, pago = pago_venta)

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

if __name__=='__main__':
    app.run(debug=True, port=3000)