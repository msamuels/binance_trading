import sys, getopt

from binance.client import Client
from binance.enums   import *


client = Client(API_KEY,
                API_PASSWORD)
"""
info = sys.argv
arglist = info[1:]

unixOptions = "s:p:q:"
gnuOptions = ["s=", "p=", "q=", "ot="]

print(info[1])
sys.exit(0)
#r = client.get_all_orders(symbol='BNBBTC', requests_params={'timeout': 5})
#print(r)
"""

#symbol = 'FETUSDT'
#symbol = 'MDAETH'
#symbol = 'XRPETH'
symbol = 'ASTETH'

#Trade fee
fees = client.get_trade_fee(symbol=symbol)
print(fees)
sys.exit(0)

for key in fees:
    for d in fees[key]:
        print(d['maker'])
        print(d['taker'])

# balance
sys.exit(0)
    
#TETHER: USDT
tether_balance = client.get_asset_balance(asset='USDT')
tether_balance['free']

#ETH
eth_balance = client.get_asset_balance(asset='ETH')
eth_balance['free']


# TODO: find symbols moving over x percent

price = 148.05
quantity = 0.08548 #.00009 less than buy price
#order_type = SIDE_BUY
order_type = SIDE_SELL

# Sell symbol
order = client.create_order(
    symbol=symbol,
    side=order_type,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=quantity,
    price=price)


"""order = client.get_order(
    symbol='MCOETH',
    orderId='orderId')
"""

for oid in order:
    print(order[oid])


#klines = client.get_historical_klines("ETHUSD", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

#print(klines)
