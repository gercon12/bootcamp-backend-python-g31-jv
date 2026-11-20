from db import db
from sqlalchemy import Integer, DateTime, float
from sqlalchemy.orm import Mapped, mapped_column


class PedidosModel(db.Model):
    id_pedido: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_cliente: Mapped[int] = mapped_column(Integer, nullable=False)
    id_plato: Mapped[int] = mapped_column(Integer, nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    total: Mapped[float] = mapped_column(float, nullable=False)

    id_cliente: Mapped[int] = mapped_column(Integer, db.ForeignKey("clientes.id_cliente"), nullable=False)
    id_plato: Mapped[int] = mapped_column(Integer, db.ForeignKey("platos.id_plato"), nullable=False)
    

    __tablename__ = "pedidos"