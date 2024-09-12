import time


class Order:
    def __init__(self, order_id, price, quantity, side, timestamp=None, order_type='limit'):
        self.order_id = order_id
        self.side = side  # buy or sell
        self.price = price  # price at which order is placed
        self.quantity = quantity
        self.order_type = order_type  # limit,market,stop
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __repr__(self):
        return f"Order(id={self.order_id},price={self.price},quantity={self.quantity},side={self.side},type={self.order_type})"
