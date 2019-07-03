import unittest
from unittest.mock import Mock
from unittest.mock import patch
from app.models import binance_trade


class TestBinanceTradeMethods(unittest.TestCase):

    def test_process_args(self):
        pass

    def test_get_all_orders(self):
        pass

    @patch('app.models.binance_trade.Client')
    def test_get_trade_fee(self, mock_client):

        client = Mock()

        mock_client.get_trade_fee('test')
        binance_trade.BinanceTrade.get_trade_fee(client, mock_client)

        assert mock_client.get_trade_fee.called_with('test')

    def test_get_symbol_balance(self):
        pass

    def test_create_order(self):
        pass


if __name__ == '__main__':
    unittest.main()
