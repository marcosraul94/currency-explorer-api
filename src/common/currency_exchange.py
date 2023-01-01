class CurrencyExchange:
    def __init__(self, dollar_buy, dollar_sell, euro_buy, euro_sell):
        self.__dollar_buy = dollar_buy
        self.__dollar_sell = dollar_sell

        self.__euro_buy = euro_buy
        self.__euro_sell = euro_sell

    def get(self):
        return {
            'dollar': {
                'buy': self.__dollar_buy,
                'sell': self.__dollar_sell,
            },
            'euro': {
                'buy': self.__euro_buy,
                'sell': self.__euro_sell,
            }
        }
