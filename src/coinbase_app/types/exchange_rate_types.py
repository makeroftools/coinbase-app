from typing import Any
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse


class GetExchangeRatesResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data = response.pop('data')
        super().__init__(**response)