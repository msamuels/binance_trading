import sys
from app.models import binance_trade

if __name__ == '__main__':
    info = sys.argv
        
    if len(info) > 3:
        symbol_to_purchase = info[1]
        p = info[2]    
        q = info[3]

        binance_trade.main(symbol_to_purchase, p, q)

    else:
        print("Missing arguments")

    sys.exit()

