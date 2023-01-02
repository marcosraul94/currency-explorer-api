import requests as r
from src.common.scraper import Scraper
from src.common.currency_exchange import CurrencyExchange
from src.common.bank_ids import bank_ids


def scrape() -> CurrencyExchange:
    url = 'https://popularenlinea.com/_api/web/lists/getbytitle(\'Rates\')/items?$filter=ItemID%20eq%20%271%27'
    headers = {'user-agent': 'n/a', 'accept': 'application/json; odata=verbose'}

    res = r.get(url, headers=headers)
    d = res.json()['d']['results'][0]

    return CurrencyExchange(
        dollar_buy=d['DollarBuyRate'],
        dollar_sell=d['DollarSellRate'],
        euro_buy=d['EuroBuyRate'],
        euro_sell=d['EuroSellRate'],
    )


popular_scraper = Scraper(scrape, bank_ids.popular)
