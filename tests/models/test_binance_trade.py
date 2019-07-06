import unittest
from unittest.mock import Mock
from unittest.mock import patch
from app.models import binance_trade


class TestBinanceTradeMethods(unittest.TestCase):

    def test_process_args(self):
        pass

    def test_get_all_orders(self):
        mock_client = Mock()

        binance_trade.get_all_orders(mock_client, 'symbol')

        mock_client.get_all_orders.assert_called_with(requests_params={'timeout': 5}, symbol='symbol')

    def test_get_trade_fee(self):

        mock_client = Mock()

        binance_trade.get_trade_fee(mock_client, 'symbol')

        mock_client.get_trade_fee.assert_called_with(symbol='symbol')

    def test_get_asset_balance(self):
        mock_client = Mock()

        binance_trade.get_asset_balance(mock_client, 'symbol')

        mock_client.get_asset_balance.assert_called_with(asset='symbol')

    def test_create_order(self):
        mock_client = Mock()
        binance_trade.create_order(mock_client, 'symbol', 'order_type', 'quantity', 'price')

        mock_client.create_order.assert_called_with(symbol='symbol',
                                                    side='order_type',
                                                    type='LIMIT',
                                                    timeInForce='GTC',
                                                    quantity='quantity',
                                                    price='price')
        

    def test_is_balance_enough(self):
        balance = 5
        assert binance_trade.is_balance_enough(balance) == 0


if __name__ == '__main__':
    unittest.main()
