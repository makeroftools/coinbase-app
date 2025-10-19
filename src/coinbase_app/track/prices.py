from typing import Any
from coinbase_app.constants import API_PREFIX
from coinbase_app.types.price_types import (
    GetBuyPriceResponse,
    GetSellPriceResponse,
    GetSpotPriceResponse
)

def get_buy_price(self, currency_pair: str, **kwargs)-> GetBuyPriceResponse:
    endpoint: str = f"{API_PREFIX}/prices/{currency_pair}/buy"
    return GetBuyPriceResponse(self.get(endpoint,**kwargs))

def get_sell_price(self, currency_pair: str, **kwargs)-> GetsellPriceResponse:
    endpoint: str = f"{API_PREFIX}/prices/{currency_pair}/sell"
    return GetSellPriceResponse(self.get(endpoint,**kwargs))

def get_spot_price(self, currency_pair: str, **kwargs)-> GetspotPriceResponse:
    endpoint: str = f"{API_PREFIX}/prices/{currency_pair}/spot"
    return GetSpotPriceResponse(self.get(endpoint,**kwargs))