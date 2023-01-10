import requests as r
from datetime import date
from src.common.scraper import Scraper
from src.common.bank_ids import bank_ids
from src.common.models import Exchange


def scrape() -> Exchange:
    url = 'https://popularenlinea.com/_api/web/lists/getbytitle(\'Rates\')/items?$filter=ItemID%20eq%20%271%27'
    headers = {'user-agent': 'n/a', 'accept': 'application/json; odata=verbose'}

    res = r.get(url, headers=headers)
    d = res.json()['d']['results'][0]

    return Exchange(
        date=date.today(),
        dollar_buy=d['DollarBuyRate'],
        dollar_sell=d['DollarSellRate'],
        euro_buy=d['EuroBuyRate'],
        euro_sell=d['EuroSellRate'],
        bank_id=bank_ids.popular,
    )


popular_scraper = Scraper(scrape, bank_ids.popular)
