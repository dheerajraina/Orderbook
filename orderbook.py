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

    def display_order_book(self):
        print(
            f"{'Price':<10}{'Side':<8}{'Quantity':<10}{'|':<3}{'Price':<10}{'Side':<8}{'Quantity'}")
        print("-" * 50)

        # -price for descending
        buy_orders = sorted(
            self.buy_orders, key=lambda x: (-x[0], x[1]), reverse=True)
        sell_orders = sorted(self.sell_orders, key=lambda x: (
            x[0], x[1]))

        # Max length b/w buy and sell for row alignment
        max_len = max(len(buy_orders), len(sell_orders))
        for i in range(max_len):
            buy_line = ""
            sell_line = ""

            if i < len(buy_orders):
                buy_order = buy_orders[i][2]  # Get the actual Order object
                buy_line = f"{buy_order.price:<10}{'BUY':<8}{buy_order.quantity:<10}"

            if i < len(sell_orders):
                sell_order = sell_orders[i][2]  # Get the actual Order object
                sell_line = f"{sell_order.price:<10}{'SELL':<8}{sell_order.quantity:<10}"

            print(f"{buy_line:<30}| {sell_line}")

    def handle_new_order(self, order):
        self.add_order(order)
