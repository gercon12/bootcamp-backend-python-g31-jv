
from db import db
from sqlalchemy import Integer, String  
from sqlalchemy.orm import Mapped, mapped_column

#db.Model indica que esta clase es una tabla
class ClientesModel(db.Model):
    #Sintaxis antigua
    # id = db.Column(db.Integer, primary_key=True)

    id_cliente: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    telefono: Mapped[str] = mapped_column(String(9), nullable=False)
    direccion: Mapped[str] = mapped_column(String(200), nullable=False)

    # para nombrar a tu tabla __tablename__ = "clientes"
    __tablename__ = "clientes"

