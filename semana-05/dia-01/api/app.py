from flask import Flask
import psycopg2

# vamos a conetar nuestro servidor API con la bd
# debes tener instalado psycopg2 = > PostgreSQL. mysqlclient = > MySQL. pymongo = > MongoDB
# pip install psycopg2


# conexion
# vamos a crear una funcion para conectarnos a la base de datos
# informacion o los datos que vas enviar son los siguientes:
# host = es el lugar donde esta alojada la base de datos (localhost)
# database = es el nombre de la base de datos (nombre de la bd)
# user = es el nombre del usuario (postgres)
# password = es la contraseña del usuario (root)
# port = es el puerto de la base de datos (5433)
app = Flask(__name__)

def get_db_connection():
    conexion = psycopg2.connect(
        host="localhost",
        database="canciones",
        user="postgres",
        password="root",
        port="5433"
    )
    return conexion

@app.route('/api/artistas', methods=['GET'])
def get_artistas():
    # 01. conectar a la base de datos
    conn = get_db_connection()
    # 02. crear un cursor para ejecutar consultas podemos ejecutar sql
    cur = conn.cursor()
    # 03. ejecutar la consulta sql para obtener todos los artistas
    cur.execute("SELECT * FROM artistas;")
    # 04. guardar los resultados de la consulta en una variable
    artistas = cur.fetchall()
    # 05. cerrar el cursor
    cur.close()
    # 06. cerrar la conexion
    conn.close()

    print(artistas)
    return 

app.run(debug=True)