
from flask import Flask, send_file, render_template
import jinja2
import pymysql

conection=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project"
)

app=Flask(__name__,template_folder='templates')

@app.route('/Login')
def Login():
    return send_file('./templates/indice.html')

@app.route('/Productos')
def Productos():
    with conection.cursor() as cursor:
        # Obtener todos los datos de la tabla
        cursor.execute("SELECT * FROM producto")
        resultado=cursor.fetchall()
    return render_template('Productos.html',resultado=resultado)

@app.route('/Clientes')
def Clientes():
    with conection.cursor() as cursor:
        # Obtener todos los datos de la tabla
        cursor.execute("SELECT * FROM cliente")
        cliente=cursor.fetchall()
    return render_template('Clientes.html',cliente=cliente)
    # return send_file('./templates/Clientes.html')

@app.route('/Ventas')
def Ventas():
    with conection.cursor() as cursor:
        # Obtener todos los datos de la tabla
        cursor.execute("SELECT * FROM venta")
        Ventas=cursor.fetchall()
    return render_template('Ventas.html',Ventas=Ventas)
    # return send_file('./templates/Ventas.html')
app.run(debug=True)

