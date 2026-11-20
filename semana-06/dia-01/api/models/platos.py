from db import db
from sqlalchemy import Integer, String, float  
from sqlalchemy.orm import Mapped, mapped_column


class PlatosModel(db.Model):
    id_plato: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    categoria: Mapped[str] = mapped_column(String(100), nullable=False)
    precio: Mapped[float] = mapped_column(nullable=False)

    __tablename__ = "platos"
