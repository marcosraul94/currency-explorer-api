from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.utils.testing import mock_request_method
from src.scrapers.popular.scraper import popular_scraper


class TestPopularScraper(TestCase):
    @patch('src.scrapers.popular.scraper.r.get')
    def test_returns_correct_shape(self, mock_get: MagicMock):
        mock_response = {
            'd': {'results': [{
                'DollarBuyRate': 1,
                'DollarSellRate': 2,
                'EuroBuyRate': 3,
                'EuroSellRate': 4,
            }]}
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
        currency_exchange = popular_scraper()

        self.assertEqual(currency_exchange.get(), expected_response)
