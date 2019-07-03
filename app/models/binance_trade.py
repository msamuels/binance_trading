import sys
import getopt
import config

from binance.client import Client
from binance.enums import *


class BinanceTrade:

    def __init__(self, symbol, price, quantity, order_type):
        """Hello World client constructor

        :return:
        """

        self.API_KEY = config.API_KEY
        self.API_SECRET = config.API_SECRET
        self.symbol = symbol #'ASTETH'
        self.price = price #148.05
        self.quantity = quantity #0.08548  # .00009 less than buy price
        # order_type = SIDE_BUY
        self.order_type = order_type #SIDE_SELL

        self.client = Client(config.API_KEY, config.API_SECRET)

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

    def get_all_orders(self, client):
        """Get all orders
        :return:
        """

        r = client.get_all_orders(symbol=self.symbol, requests_params={'timeout': 5})
        print(r)

    def get_trade_fee(self, client):
        """ Get fee for trade

        :returns: list of dictionaries containing "maker"(bid), "taker"(ask) and "symbol" keys
        """

        """
        for key in fees:
            for d in fees[key]:
                print(d['maker'])
                print(d['taker'])
        """

        fees = client.get_trade_fee(symbol=self.symbol)
        print(fees['tradeFee'])

        return fees['tradeFee']

    def get_symbol_balance(self, client):
        """Get account balance for the given symbol

        :return: dictionary with asset balance "free" as float
        """

        # ETH
        eth_balance = client.get_asset_balance(asset=self.symbol)
        return eth_balance['free']

    def create_order(self, client):
        """Create a sell or buy order
        @TODO: find symbols moving over x percent
        :return:
        """

        # Sell symbol
        order = client.create_order(
            symbol=self.symbol,
            side=self.order_type,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=self.quantity,
            price=self.price)

        """order = client.get_order(
            symbol='MCOETH',
            orderId='orderId')
        """

        for oid in order:
            print(order[oid])

    def get_klines(self, client):
        """ Get klines
        :return:
        """

        klines = client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
        return klines
