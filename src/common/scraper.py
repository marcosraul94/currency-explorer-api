from typing import Callable
from src.common.currency_exchange import CurrencyExchange


class Scraper:
    def __init__(self, scrape: Callable, bank_name: str):
        self.scrape = scrape
        self.bank_name = bank_name

    def __call__(self) -> CurrencyExchange:
        self.log('Scraping...')
        currency_exchange: CurrencyExchange = self.scrape()
        self.log(f'Currency exchange response: {currency_exchange.get()}')

        return currency_exchange

    def log(self, message):
        print(f'***{self.bank_name} Scraper***', message)
