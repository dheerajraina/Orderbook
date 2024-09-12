import heapq


class OrderBook:
    def __init__(self):
        self.buy_orders = []  # arranged in descending order -> Max heap
        self.sell_orders = []  # arranged in ascending order -> Min heap
        self.trades = []  # stores all the trades
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
        if order.order_type == "market":
            return self.handle_market_order(order)
        else:
            self.add_order(order)

    def handle_market_order(self, order):
        # Market Orders match immediately with the opposite side
        if order.side == "buy":
            if not self.sell_orders:
                print(
                    f"Market buy order {order.order_id} rejected: No liquidity available")
                return
            while order.quantity > 0 and self.sell_orders:
                best_sell = self.sell_orders[0][2]
                traded_quantity = min(order.quantity, best_sell.quantity)
                self.trades.append((order.order_id, best_sell.order_id,
                                    traded_quantity, best_sell.price))
                order.quantity -= traded_quantity
                best_sell.quantity -= traded_quantity

                if best_sell.quantity == 0:
                    heapq.heappop(self.sell_orders)

        else:  # market sell orders
            if not self.buy_orders:
                print(
                    f"Market sell order {order.order_id} rejected: No liquidity available")
                return
            while order.quantity > 0 and self.buy_orders:
                best_buy = self.buy_orders[0][2]
                traded_quantity = min(order.quantity, best_buy.quantity)
                self.trades.append((best_buy.order_id, order.order_id,
                                    traded_quantity, best_buy.price))
                order.quantity -= traded_quantity
                best_buy.quantity -= traded_quantity

                if best_buy.quantity == 0:
                    heapq.heappop(self.buy_orders)
