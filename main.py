from flask import Flask, render_template, request

# Libreria de protección
from flask_wtf import CSRFProtect
# Libreria para mensajes flash
from flask import flash
# Libreria para cookies
from flask import make_response
# Libreria para variables globales
from flask import g

# Clases desarrolladas
import forms
import venta
import consultas


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
        fecha = venta_form.fecha_venta.data
        cliente = venta_form.nombre_cliente.data
        
        venta_class = venta.Venta(compradores, tikets, tarjeta, fecha, cliente)
        
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

@app.route('/consulta', methods = ['GET', 'POST'])
def consulta():
    
    consulta_form = forms.ConsultaForm(request.form)
    nombre_empleado = request.cookies.get('nombre_empleado')
    lista = []
    total = 0
    
    if request.method == 'POST' and consulta_form.validate():
        
        dia = consulta_form.dias.data
        mes = consulta_form.meses.data
        tipo_consulta = consulta_form.tipo_consulta.data
        
        consulta_class = consultas.Consulta(dia, mes, tipo_consulta)
        lista = consulta_class.realizarConsulta()
        total = consulta_class.obtener_totalVentas(lista)
        #lista = consulta_class.consultarVentasMes()
    
    return render_template('consulta.html', form = consulta_form, empleado = nombre_empleado, lista = lista, total = total)

if __name__=='__main__':
    app.run(debug=True, port=3000)