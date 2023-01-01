import requests as r
from src.common.scraper import Scraper
from src.common.currency_exchange import CurrencyExchange


def scrape() -> CurrencyExchange:
    url = 'https://popularenlinea.com/_api/web/lists/getbytitle(\'Rates\')/items?$filter=ItemID%20eq%20%271%27'
    headers = {'user-agent': 'n/a', 'accept': 'application/json; odata=verbose'}

    res = r.get(url, headers=headers)
    data = res.json()['d']['results'][0]

    return CurrencyExchange(
        dollar_buy=data['DollarBuyRate'],
        dollar_sell=data['DollarSellRate'],
        euro_buy=data['EuroBuyRate'],
        euro_sell=data['EuroSellRate'],
    )


popular_scraper = Scraper(scrape, 'Popular scraper')
