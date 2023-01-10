from datetime import date
from unittest.mock import patch, MagicMock
from src.common.models import Exchange
from src.utils.testing import mock_request_method, UnitTest
from src.scrapers.banreservas.scraper import banreservas_scraper, Scraper, bank_ids


class TestBanreservasScraper(UnitTest):
    @patch.object(Scraper, 'save')
    @patch('src.scrapers.banreservas.scraper.r.get')
    def test_returns_correct_shape(self, mock_get: MagicMock, mock_save: MagicMock):
        mock_response = {
            'compraUS': 1,
            'ventaUS': 2,
            'compraEU': 3,
            'ventaEU': 4,
         }
        mock_get.return_value = mock_request_method(mock_response)
        mock_save.side_effect = lambda exchange: exchange

        expected_response = Exchange(
            date=date.today(),
            dollar_buy=1,
            dollar_sell=2,
            euro_buy=3,
            euro_sell=4,
            bank_id=bank_ids.banreservas
        )
        response = banreservas_scraper()

        self.assertEqualExchange(response, expected_response)
