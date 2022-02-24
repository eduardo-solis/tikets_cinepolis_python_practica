from wtforms import Form
from wtforms import StringField ,IntegerField, RadioField, DateField
from wtforms.validators import InputRequired, NumberRange, ValidationError

class VentaForm(Form):
    
    nombre = StringField('Nombre', validators=[InputRequired('Se requiere ingresar un nombre')])
    cantidad_compradores = IntegerField('Cantidad de compradores', validators=[NumberRange(min=1, message='Se requiere por lo menos 1 comprador'), InputRequired('Se requiere ingresar un valor')])
    tarjeta_descuento = RadioField('Tarjeta de descuento', default='0',
                                choices=[('1','Si'), ('0', 'No')])
    cantidad_tikets = IntegerField('Cantidad de tikets', validators=[NumberRange(min=1, message='Se requiere por lo menos 1 tiket'), InputRequired('Se requiere ingresar un valor')])
    fecha_venta = DateField('Fecha de venta', validators=[InputRequired('Se requiere ingresar una fecha')])

