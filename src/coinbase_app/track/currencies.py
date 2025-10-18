from typing import Any 
from coinbase_app.adv_trade.constants import API_PREFIX
from coinbase_app.types.currency_types import FiatCurrenciesResponse
from coinbase_app.types.currency_types import CryptoCurrenciesResponse



def get_fiat_currencies(
    self,
    **kwargs
) -> FiatCurrenciesResponse:
    endpoint = f"{API_PREFIX}/currencies"
    return FiatCurrenciesResponse(self.get(endpoint, **kwargs))

def get_crypto_currencies(
    self,
    **kwargs
) -> CryptoCurrenciesResponse:
    endpoint: str = f"{API_PREFIX}/currencies/crypto"
    return CryptoCurrenciesResponse(self.get(endpoint, **kwargs))



