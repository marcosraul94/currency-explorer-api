from typing import Callable
from src.common.currency_exchange import CurrencyExchange


class Scraper:
    def __init__(self, scrape: Callable, name: str):
        self.scrape = scrape
        self.name = name

    def __call__(self) -> CurrencyExchange:
        self.log('Scraping...')
        currency_exchange: CurrencyExchange = self.scrape()
        self.log(f'Currency exchange response: {currency_exchange.get()}')

        return currency_exchange

    def log(self, message):
        print(f'***{self.name}***', message)
