import requests as r
from datetime import date
from src.common.scraper import Scraper
from src.common.models import Exchange
from src.common.bank_ids import bank_ids


def scrape() -> Exchange:
    url = 'https://www.banreservas.com/_layouts/15/SharePointAPI/ObtenerTasas.ashx'
    headers = {'user-agent': 'n/a', 'accept': 'application/json, text/javascript, */*; q=0.01'}

    res = r.get(url, headers=headers)
    d = res.json()

    return Exchange(
        date=date.today(),
        dollar_buy=d['compraUS'],
        dollar_sell=d['ventaUS'],
        euro_buy=d['compraEU'],
        euro_sell=d['ventaEU'],
        bank_id=bank_ids.banreservas,
    )


banreservas_scraper = Scraper(scrape, bank_ids.banreservas)
