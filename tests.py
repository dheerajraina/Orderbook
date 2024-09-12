import random
import time
import threading
from order import Order
from orderbook import OrderBook


def test_order_book():
    order_book = OrderBook()

    def test_cancel_order(side, input_range):
        random_id = f"{side}_{random.randint(1, input_range)}"
        order_book.cancel_order(random_id)

    def test_modify_order(side, input_range):
        random_id = f"{side}_{random.randint(1, input_range)}"
        new_price = random.randint(1, 100)
        new_quantity = random.randint(1, 1000)
        order_book.modify_order(random_id, new_price, new_quantity)

    def push_buy_orders():
        for i in range(1000):
            time.sleep(1)
            price = random.randint(1, 100)
            quantity = random.randint(1, 1000)
            order_type = random.choice(['market', 'limit', 'stop'])
            new_order = Order(
                order_id=f'buy_{i}', price=price, quantity=quantity, side='buy', order_type=order_type)
            order_book.handle_new_order(new_order)

            if i > 10:
                test_cancel_order('buy', i)
                test_modify_order("buy", i)

    def push_sell_orders():
        for i in range(1000):
            time.sleep(1)
            price = random.randint(0, 100)
            quantity = random.randint(1, 1000)
            order_type = random.choice(['market', 'limit', 'stop'])
            new_order = Order(
                order_id=f'sell_{i}', price=price, quantity=quantity, side='sell', order_type=order_type)
            order_book.handle_new_order(new_order)

            order_book.display_order_book()

            if i > 10:
                test_cancel_order('sell', i)
                test_modify_order("sell", i)

    thread_buy = threading.Thread(target=push_buy_orders)
    thread_sell = threading.Thread(target=push_sell_orders)

    thread_buy.start()
    thread_sell.start()

    thread_buy.join()
    thread_sell.join()

    print(f"Executed {len(order_book.trades)} trades")


test_order_book()
