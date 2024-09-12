import random
import time
import threading
from order import Order
from orderbook import OrderBook


def test_order_book():
    order_book = OrderBook()

    def push_buy_orders():
        for i in range(100):
            time.sleep(1)
            price = random.randint(0, 100)
            quantity = random.randint(0, 1000)
            order_type = random.choice(['market', 'limit', 'stop'])
            new_order = Order(
                order_id=f'buy{i}', price=price, quantity=quantity, side='buy', order_type=order_type)
            order_book.handle_new_order(new_order)
            order_book.display_order_book()

    def push_sell_orders():
        for i in range(100):
            time.sleep(1)
            price = random.randint(0, 100)
            quantity = random.randint(0, 1000)
            order_type = random.choice(['market', 'limit', 'stop'])
            new_order = Order(
                order_id=f'sell_{i}', price=price, quantity=quantity, side='sell', order_type=order_type)
            order_book.handle_new_order(new_order)
            order_book.display_order_book()

    thread_buy = threading.Thread(target=push_buy_orders)
    thread_sell = threading.Thread(target=push_sell_orders)

    thread_buy.start()
    thread_sell.start()

    thread_buy.join()
    thread_sell.join()

    print(f"Executed {len(order_book.trades)} trades")


test_order_book()
