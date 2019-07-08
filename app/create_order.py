# python create_order.py symbol price quanity
# python create_order.py ETHUSDT 300.00 1

import sys
from app.logic import create_execute_buy

if __name__ == '__main__':
    info = sys.argv
        
    if len(info) > 3:
        symbol_to_purchase = info[1]
        p = info[2]    
        q = info[3]

        create_execute_buy.main(symbol_to_purchase, p, q)

    else:
        print("Missing arguments")

    sys.exit()

