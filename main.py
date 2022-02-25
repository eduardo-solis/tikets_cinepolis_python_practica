from flask import Flask, render_template, request
import forms
import venta


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    venta_form = forms.VentaForm(request.form)
    mensaje_venta = ''
    
    if request.method == 'POST' and venta_form.validate():
        print(venta_form.nombre.data)
        print(venta_form.cantidad_compradores.data)
        print(venta_form.tarjeta_descuento.data)
        print(venta_form.cantidad_tikets.data)
        print(venta_form.fecha_venta.data)
        
        compradores = venta_form.cantidad_compradores.data
        tikets = venta_form.cantidad_tikets.data
        tarjeta = venta_form.tarjeta_descuento.data
        
        venta_class = venta.Venta(compradores, tikets, tarjeta)
        
        mensaje_venta = venta_class.realizarVenta()
    
    return render_template('venta.html', form = venta_form, mensaje = mensaje_venta)

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

if __name__=='__main__':
    app.run(debug=True, port=3000)