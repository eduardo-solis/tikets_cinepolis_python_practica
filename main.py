from flask import Flask, render_template, request

# Libreria de protección
from flask_wtf import CSRFProtect
# Libreria para mensajes flash
from flask import flash
# Libreria para cookies
from flask import make_response

# Clases desarrolladas
import forms
import venta


app = Flask(__name__)

# Creación de la protección
app.secret_key = 'clave_secreta'
csrf = CSRFProtect(app)

@app.errorhandler(code_or_exception=404)
def page_not_found(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    print('Paso 1')

@app.after_request
def after_request(response):
    print('Paso 3')
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    print('Paso 2')
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
    
    response = make_response(render_template('venta.html', form = venta_form, pago = pago_venta))
    response.set_cookie('nombre_empleado','Eduardo')
    return response
    
    #return render_template('venta.html', form = venta_form, pago = pago_venta)

@app.route('/consulta')
def consulta():
    nombre_empleado = request.cookies.get('nombre_empleado')
    return render_template('consulta.html', empleado = nombre_empleado)

if __name__=='__main__':
    app.run(debug=True, port=3000)