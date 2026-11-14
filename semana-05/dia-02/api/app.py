from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)





# configure the SQLite database, relative to the app instance folder
# Conexion con nuestra BD
# Configuracion de las credenciales de la BD
# DIALECT://USERNAME:PASSWORD@HOST:PORT/DATABASE
# Ejemplo: postgresql://postgres:admin@localhost:5432/mi_bd
# postgresql://postgres:root@localhost:5433/canciones
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/canciones"

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

    def to_dict(self):
            return {
                "id": self.id,
                "nombre": self.nombre,
                "genero": self.genero,
                "pais_origen": self.pais_origen,
                "activo": self.activo,
                "fecha_creacion": self.fecha_creacion
            }

class Canciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    album = db.Column(db.String(150), nullable=False)
    duracion_segundos = db.Column(db.Integer, nullable=False)  # Duración en segundos
    anio_lanzamiento = db.Column(db.Integer, nullable=False)  # Año de lanzamiento
    artista_id = db.Column(db.Integer, db.ForeignKey('artistas.id'), nullable=False)
    
    # Especificar el nombre de la tabla en la base de datos
    __tablename__ = "canciones" #nombre en base de datos postgresql

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "album": self.album,
            "duracion_segundos": self.duracion_segundos,
            "anio_lanzamiento": self.anio_lanzamiento,
            "artista_id": self.artista_id
        }

    

# # Se solicita crear endpoint, para obener todos los artistas de la base de datos
# @app.route('/api/artistas', methods=['GET'])
# def get_artistas():
#     artistas = Artistas.query.all()
#     artistas_list = []
#     for artista in artistas:
#         artistas_list.append({
#             'id': artista.id,
#             'nombre': artista.nombre,
#             'genero': artista.genero,
#             'pais_origen': artista.pais_origen,
#             'activo': artista.activo
#         })
#     return {'artistas': artistas_list}

# # Se solicita crear endpoint, para obener todos los artistas de la base de datos
# @app.route('/api/canciones', methods=['GET'])
# def get_canciones():
#     canciones = Canciones.query.all()
#     canciones_list = []
#     for cancion in canciones:
#         canciones_list.append({
#             'id': cancion.id,
#             'titulo': cancion.titulo,
#             'album': cancion.album,
#             'duracion_segundos': cancion.duracion_segundos,
#             'anio_lanzamiento': cancion.anio_lanzamiento,
#             'artista_id': cancion.artista_id
#         })
#     return {'canciones': canciones_list}

@app.route("/api/artistas", methods=["GET"])
def get_artistas():
    # 01. Hacer la consulta
    artistas = Artistas.query.all()

    # [Artistas1, Artistas2]
    # print(artistas[2].nombre)

    resultado_formateado = []
    for elm in artistas:
        # formato = {
        #     "id": elm.id,
        #     "nombre": elm.nombre,
        #     "genero": elm.genero
        # }
        resultado_formateado.append(elm.to_dict())


    return {
        "data": resultado_formateado
    }

# reto 02
# crear el endpoint /api/canciones
# el cual devuelte todas las canciones
# no devolver artista_id

@app.route("/api/canciones", methods=["GET"])
def get_canciones():
    canciones = Canciones.query.all()

    resultado_formateado=[]
    for elm in canciones:
        resultado_formateado.append(elm.to_dict())

    return {
        "msg": "canciones encontradas",
        "data": resultado_formateado
    }


# Necesitamos que se devuelva a un solo artista
# Se cree un endpoint el cual devuelva al artista segun el id
#  /api/artistas/<id>
# este endpoint tiene que ser del tipo GET
@app.route("/api/artistas/<int:id>", methods=["GET"])
def get_single_artist(id):
    # 01. Realizar tu consulta
    artista = Artistas.query.get(id)
    # <Artista>
    if artista is None:
        return {
            "msg": "Artista no encontrado"
        }, 404

    return artista.to_dict()

# solicita que se cree un endpoint => /api/add-artistas
# Tiene que ser del tipo POST => Insertar informacion
# INSERT INTO artistas ( COL ) VALUES ()
@app.route("/api/add-artistas", methods=["POST"])
def add_artistas():
    # Vas a capturar el JSON que te va enviar el frontend
    # {
    #    "nombre": "Rafaga",
    #    "genero": "Cumbia",
    #    "pais_origen": "Argentina"
    # }
    # 01. Capturar la informacion
    data = request.json

    # 02. Validaciones
    if not data:
        return {
            "msg": "Debes de enviar la informacion"
        }

    # 03. Crear una instancia de como se insertara
    # el registro en la bd
    nuevo_artista = Artistas(
        nombre=data["nombre"],
        genero=data["genero"],
        pais_origen=data.get("pais_origen")
    )

    # 04. Ejecutar y confirmar (guardar)
    db.session.add(nuevo_artista)
    db.session.commit()

    return {
        "msg": "Creacion exitosa"
    }, 201

# Eliminar un artista por su id
# /api/del-artistas/id
@app.route("/api/del-artistas/<int:id>", methods=["DELETE"])
def delete_artista(id):
    #  01. Consulta
    artista = Artistas.query.get(id)

    # 02. Validaciones
    if artista is None:
        return {
            "msg": "Artista no encontrado"
        }

    # 03. Eliminacion de la BD
    db.session.delete(artista)
    db.session.commit()

    return{
        "msg": "Artista eliminado exitosamente"
    }, 200