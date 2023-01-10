from typing import Callable
from src.common.models import Exchange
from src.common.app import context, session


class Scraper:
    def __init__(self, scrape: Callable, bank_name: str):
        self._scrape = scrape
        self.bank_name = bank_name

    def __call__(self) -> Exchange:
        exchange = self.scrape()

        return self.save(exchange)

    def log(self, *args):
        print(f'***{self.bank_name} Scraper***', *args)

    def scrape(self) -> Exchange:
        self.log('Scraping...')
        exchange = self._scrape()
        self.log('Scraping response:', exchange)

        return exchange

    def save(self, exchange: Exchange) -> Exchange:
        self.log('Saving...')

        with context():
            session.add(exchange)
            session.commit()
            session.refresh(exchange)

        self.log('Saved completed:', exchange)

        return exchange
