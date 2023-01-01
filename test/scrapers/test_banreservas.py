from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.utils.testing import mock_request_method
from src.scrapers.banreservas.scraper import banreservas_scraper


class TestBanreservasScraper(TestCase):
    @patch('src.scrapers.banreservas.scraper.r.get')
    def test_returns_correct_shape(self, mock_get: MagicMock):
        mock_response = {
            'compraUS': 1,
            'ventaUS': 2,
            'compraEU': 3,
            'ventaEU': 4,
         }

        mock_get.return_value = mock_request_method(mock_response)
        expected_response = {
            'dollar': {
                'buy': 1,
                'sell': 2,
            },
            'euro': {
                'buy': 3,
                'sell': 4,
            }
        }
        currency_exchange = banreservas_scraper()

        self.assertEqual(currency_exchange.get(), expected_response)
