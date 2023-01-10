from datetime import date
from src.scrapers.popular.scraper import popular_scraper
from src.utils.testing import E2ETest


class TestPopularScraper(E2ETest):
    def test_returns_valid_data(self):
        exchange = popular_scraper()

        self.assertIsNotNone(exchange)
        self.assertEqual(exchange.date, date.today())
        self.assertIsNotNone(exchange.dollar_buy)
        self.assertIsNotNone(exchange.dollar_sell)
        self.assertIsNotNone(exchange.euro_buy)
        self.assertIsNotNone(exchange.euro_sell)
