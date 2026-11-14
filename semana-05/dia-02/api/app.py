from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)





# configure the SQLite database, relative to the app instance folder
# Conexion con nuestra BD
# Configuracion de las credenciales de la BD
# DIALECT://USERNAME:PASSWORD@HOST:PORT/DATABASE
# Ejemplo: postgresql://postgres:admin@localhost:5432/mi_bd
# postgresql://postgres:root@localhost:5433/canciones
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5433/canciones"

# Integrar SQLAlchemy cen todo mi servidor
db = SQLAlchemy(app)

# Definir nuestro modelo (tabla) de artistas
class Artistas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    pais_origen = db.Column(db.String(50), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    fecha_creacion = db.Column(db.DateTime, server_default=db.func.now())

    # Especificar el nombre de la tabla en la base de datos
    __tablename__ = "artistas" #nombre en base de datos postgresql

class Canciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    album = db.Column(db.String(150), nullable=False)
    duracion_segundos = db.Column(db.Integer, nullable=False)  # Duración en segundos
    anio_lanzamiento = db.Column(db.Integer, nullable=False)  # Año de lanzamiento
    artista_id = db.Column(db.Integer, db.ForeignKey('artistas.id'), nullable=False)
    
    # Especificar el nombre de la tabla en la base de datos
    __tablename__ = "canciones" #nombre en base de datos postgresql

# Se solicita crear endpoint, para obener todos los artistas de la base de datos
@app.route('/api/artistas', methods=['GET'])
def get_artistas():
    artistas = Artistas.query.all()
    artistas_list = []
    for artista in artistas:
        artistas_list.append({
            'id': artista.id,
            'nombre': artista.nombre,
            'genero': artista.genero,
            'pais_origen': artista.pais_origen,
            'activo': artista.activo
        })
    return {'artistas': artistas_list}

# Se solicita crear endpoint, para obener todos los artistas de la base de datos
@app.route('/api/canciones', methods=['GET'])
def get_canciones():
    canciones = Canciones.query.all()
    canciones_list = []
    for cancion in canciones:
        canciones_list.append({
            'id': cancion.id,
            'titulo': cancion.titulo,
            'album': cancion.album,
            'duracion_segundos': cancion.duracion_segundos,
            'anio_lanzamiento': cancion.anio_lanzamiento,
            'artista_id': cancion.artista_id
        })
    return {'canciones': canciones_list}

app.run(debug=True)