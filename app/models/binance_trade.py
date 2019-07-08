from binance.client import Client
from binance.enums import *


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


def is_balance_enough(balance):
    if balance > 10:
        return 1
    else:
        return 0

