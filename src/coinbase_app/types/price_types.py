from typing import Any
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse


class GetBuyPriceResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response)

class GetSellPriceResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response)

class GetSpotPriceResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response)