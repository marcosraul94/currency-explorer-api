import requests as r
from src.common.scraper import Scraper
from src.common.currency_exchange import CurrencyExchange


def scrape() -> CurrencyExchange:
    url = 'https://www.banreservas.com/_layouts/15/SharePointAPI/ObtenerTasas.ashx'
    headers = {'user-agent': 'n/a', 'accept': 'application/json, text/javascript, */*; q=0.01'}

    res = r.get(url, headers=headers)
    d = res.json()

    return CurrencyExchange(
        dollar_buy=d['compraUS'],
        dollar_sell=d['ventaUS'],
        euro_buy=d['compraEU'],
        euro_sell=d['ventaEU'],
    )


banreservas_scraper = Scraper(scrape, 'Banreservas scraper')
