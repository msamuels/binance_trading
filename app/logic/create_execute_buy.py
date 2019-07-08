"""
    1) Get main token balance. ie ETH or BTC
    2) Ensure balance > $10
    3) Calculate cost of purchase + trade fee
    4) Create and submit Buy order
    5) Get order ID
    6) Submit Stop limit order 2% lower than purchase price
    7) Poll symbol price to see if > 5% of purchase
"""

from app.config import API_SECRET
from app.config import API_KEY

from binance.client import Client
from binance.enums import *

from app.models import binance_trade


def main(symbol, price, qty):
    """ Create and execute order
    Args
        symbol (str): Symbol
        price (double): Price of symbol
        qty (int): Amount to purchase
    :return:
    """

    client = Client(API_KEY, API_SECRET)

    # 1  Get main token balance.
    balance = get_asset_balance(client, 'USDT')

    # 2 Ensure balance > $10
    if is_balance_enough(balance['free']):

        # 3 Calculate cost of purchase + trade fee
        fee = get_trade_fee(client, symbol)

        # 4 Create and submit Buy order
        # 5 Get order ID
        order = create_order(client, symbol, order_type=SIDE_BUY, quantity=qty, price=price)

        # check if the order status
        if order['status'] == 'FILLED':
            # 6 Submit Stop limit order 2% lower than purchase price
            stop_limit_price = price - (price * .02)
            stop_limit_order = create_order(client, symbol, order_type=ORDER_TYPE_STOP_LOSS_LIMIT,
                                            quantity=qty, price=stop_limit_price)

