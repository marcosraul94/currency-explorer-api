from unittest import TestCase
from src.scrapers.popular.scraper import popular_scraper


class TestPopularScraper(TestCase):
    def test_returns_valid_data(self):
        exchange = popular_scraper().get()

        self.assertIsNotNone(exchange)
        self.assertIsNotNone(exchange['dollar']['buy'])
        self.assertIsNotNone(exchange['dollar']['sell'])
        self.assertIsNotNone(exchange['euro']['buy'])
        self.assertIsNotNone(exchange['euro']['sell'])
