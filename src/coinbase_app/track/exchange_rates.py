from typing import Any
from coinbase_app.constants import API_PREFIX
from coinbase_app.types.exchange_rate_types import GetExchangeRatesResponse



def get_exchange_rates(self, currency: str|None, **kwargs) -> GetExchangeRatesResponse:
    endpoint: str = f"{API_PREFIX}/exchange-rates"
    return GetExchangeRatesResponse(self.get(endpoint, **kwargs))