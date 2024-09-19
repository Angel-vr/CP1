from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL 

app=Flask(__name__)


app.config["MYSQL_HOST"]        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config["MYSQL_DB"]          = 'dbcrud'
app.config["MYSQL_CURSORCLASS"] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def index_clientes():

    sql = 'SELECT * from clientes'
    cur = mysql.connection.cursor()
    cur.execute(sql)
    clientes = cur.fetchall()

    return render_template('modulos/clientes/index.html', clientes=clientes)

@app.route('/clientes/create')
def create():
    return render_template('modulos/clientes/create.html')

@app.route('/create/guardar', methods=['POST'] )
def clientes_guardar():
    nombre      = request.form['nombre']
    telefono    = request.form['telefono']
    fecha       = request.form['fecha']

    sql         = 'INSERT INTO `clientes` (`nombre`, `telefono`, `fecha`) VALUES (%s, %s, %s)'
    datos       = (nombre, telefono, fecha)
    cur = mysql.connection.cursor()
    cur.execute(sql, datos)
    mysql.connection.commit()
    return redirect('/clientes')
    

if __name__ == '__main__':
    app.run(debug=True)