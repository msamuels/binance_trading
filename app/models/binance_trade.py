import sys
import getopt
import config

from binance.client import Client
from binance.enums import *


def process_args(self):
    """Get argruments from command line
    :return:
    """

    info = sys.argv
    arglist = info[1:]

    unixOptions = "s:p:q:"
    gnuOptions = ["s=", "p=", "q=", "ot="]

    print(info[1])
    sys.exit(0)


def get_all_orders(client, symbol):
    """Get all orders
    :return:
    """

    r = client.get_all_orders(symbol=symbol, requests_params={'timeout': 5})
    return r


def get_trade_fee(client, symbol):
    """ Get fee for trade

    :returns: l ist of dictionaries containing "maker"(bid), "taker"(ask) and "symbol" keys
    """

    """
    for key in fees:
        for d in fees[key]:
            print(d['maker'])
            print(d['taker'])
    """

    fees = client.get_trade_fee(symbol=symbol)
    # fees['tradeFee']
    return fees


def get_asset_balance(client, symbol):
    """Get account balance for the given symbol

    :return: dictionary with asset balance "free" as float
        eth_balance['free']
    """

    # ETH
    eth_balance = client.get_asset_balance(asset=symbol)
    return eth_balance


def create_order(client, symbol, order_type, quantity, price):
    """Create a sell or buy order
    @TODO: find symbols moving over x percent
    :return:
    """

    # Sell symbol
    order = client.create_order(
        symbol=symbol,
        side=order_type,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=quantity,
        price=price)

    #for oid in order:
    #    print(order[oid])
    return order


def get_order(client, symbol, orderid):
    """Get order
    :return order
    """

    order = client.get_order(
        symbol=symbol,
        orderId='orderId')

    return order


def get_klines(client, symbol):
    """ Get klines
    :return:
    """

    klines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    return klines


def main(symbol):
    """ 1) Get main token balance. ie ETH or BTC
        2) Ensure balance > $10
        3) Calculate cost of purchase + trade fee
        4) Create and submit Buy order
        5) Get order ID
        6) Submit Stop limit order 2% lower than purchase price
        7) Poll symbol price to see if > 5% of purchase

    :return:
    """

    client = Client(config.API_KEY, config.API_SECRET)

    fee = get_trade_fee(client, symbol)
    return fee


if __name__ == '__main__':
    crypto = 'ETHUSDT'
    main(crypto)
