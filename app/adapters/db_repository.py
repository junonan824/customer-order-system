from app.domain.models import Order
from app import db


class OrderRepository:
    def save(self, order: Order):
        db.session.add(order)
        db.session.commit()

    def get_by_id(self, order_id):
        return Order.query.get(order_id)
