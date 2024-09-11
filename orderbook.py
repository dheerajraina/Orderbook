import heapq


class OrderBook:
    def __init__(self):
        self.buy_orders = []  # arranged in descending order -> Max heap
        self.sell_orders = []  # arranged in ascending order -> Min heap

        # TODO -> handle order modification and cancellation as well

    def add_order(self, order):
        if order.side == "buy":
            heapq.heappush(self.buy_orders,
                           (-order.price, order.timestamp, order))
        else:
            heapq.heappush(self.sell_orders,
                           (order.price, order.timestamp, order))
