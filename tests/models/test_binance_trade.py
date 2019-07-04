import unittest
from unittest.mock import Mock
from unittest.mock import patch
from app.models import binance_trade


class TestBinanceTradeMethods(unittest.TestCase):

    def test_process_args(self):
        pass

    def test_get_all_orders(self):
        pass

    def test_get_trade_fee(self):

        mock_client = Mock()

        binance_trade.get_trade_fee(mock_client, 'symbol')

        mock_client.get_trade_fee.assert_called_with(symbol='symbol')

    def test_get_symbol_balance(self):
        pass

    def test_create_order(self):
        pass


if __name__ == '__main__':
    unittest.main()
