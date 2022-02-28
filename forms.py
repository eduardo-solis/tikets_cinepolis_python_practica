from email.policy import default
from wtforms import Form
from wtforms import StringField ,IntegerField, RadioField, DateField, SelectField
from wtforms.validators import InputRequired, NumberRange

class VentaForm(Form):
    
    nombre_cliente = StringField('Nombre del cliente', validators=[InputRequired('Se requiere ingresar un nombre')])
    
    cantidad_compradores = IntegerField('Cantidad de compradores', validators=[NumberRange(min=1, message='Se requiere por lo menos 1 comprador'), InputRequired('Se requiere ingresar un valor')])
    
    tarjeta_descuento = RadioField('Tarjeta de descuento', default='0',
                                choices=[('1','Si'), ('0', 'No')])
    
    cantidad_tikets = IntegerField('Cantidad de tikets', validators=[NumberRange(min=1, message='Se requiere por lo menos 1 tiket'), InputRequired('Se requiere ingresar un valor')])
    
    fecha_venta = DateField('Fecha de venta', validators=[InputRequired('Se requiere ingresar una fecha')])

class ConsultaForm(Form):
    
    tipo_consulta = RadioField('Tipo de consulta', default = '0', choices=[('0', 'Dia'), ('1', 'Mes')])
    
    dias = SelectField('Seleccione el dia', default = '0', 
                        choices = [('0', 'Domingo'), ('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6','Sabado')])
    
    meses = SelectField('Seleccione el mes', default = '01', 
                        choices = [('01', 'Enero'), ('02','Febrero'), ('03', 'Marzo'), ('04','Abril'), ('05','Mayo'), ('06','Junio'), ('07','Julio'), ('08','Agosto'), ('09','Septiembre'), ('10','Octubre'), ('11','Noviembre'), ('12','Diciembre')])