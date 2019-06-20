import sys, getopt

from binance.client import Client
from binance.enums import *
from trade import config


class BinanceTrade:

    def __init__(self, api_key, api_secret):
        """Hello World client constructor

        :param api_key: Api Key
        :type api_key: str.
        :param api_secret: Api Secret
        :type api_secret: str.
        :return:
        """

        self.client = Client(config.API_KEY, config.API_SECRET)
        self.symbol = 'ASTETH'
        self.price = 148.05
        self.quantity = 0.08548  # .00009 less than buy price
        # order_type = SIDE_BUY
        self.order_type = SIDE_SELL

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

    def get_all_orders(self):
        """Get all orders
        :return:
        """

        r = self.client.get_all_orders(symbol=self.symbol, requests_params={'timeout': 5})
        print(r)

    def get_trade_fee(self):
        """ Get fee for trade symbol
        """
        fees = self.client.get_trade_fee(symbol=self.symbol)
        print(fees)
        sys.exit(0)

        for key in fees:
            for d in fees[key]:
                print(d['maker'])
                print(d['taker'])

        sys.exit(0)

    def get_symbol_balance(self):
        """Get symbol balance

        :return:
        """
        tether_balance = self.client.get_asset_balance(asset=self.symbol)
        tether_balance['free']

        # ETH
        eth_balance = self.client.get_asset_balance(asset=self.symbol)
        eth_balance['free']

    def create_order(self):
        """Create a sell or buy order
        @TODO: find symbols moving over x percent
        :return:
        """

        # Sell symbol
        order = self.client.create_order(
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

    def get_klines(self):
        """ Get klines
        :return:
        """

        klines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
        return klines
