# Aqui vamos a crear nuestro archivo base (cerebro) 🧠
# Crear el servidor
from flask import Flask
from db import db  # SQLAlchemy

app = Flask(__name__)

# ⚙️ 03. Configuraciones
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# Integracion de SQLAlchemy en mi proyecto
db.init_app(app)

if __name__ == "__main__":
   app.run(debug=True)