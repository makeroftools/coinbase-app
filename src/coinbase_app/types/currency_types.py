from typing import Any 
from coinbase_app.adv_trade.constants import API_PREFIX
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse

class FiatCurrenciesResponse(BaseResponse):
    """
        {
        "data": [
            {
            "id": "AED",
            "name": "United Arab Emirates Dirham",
            "min_size": "0.01000000"
            },
            {
            "id": "AFN",
            "name": "Afghan Afghani",
            "min_size": "0.01000000"
            },
            {
            "id": "ALL",
            "name": "Albanian Lek",
            "min_size": "0.01000000"
            },
            {
            "id": "AMD",
            "name": "Armenian Dram",
            "min_size": "0.01000000"
            }
        ],
        ...
        }
    """
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: list[FiatCurrency] = [
                FiatCurrency(**fc) for fc in response.pop('data')
            ]

class FiatCurrency(BaseResponse):
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id: str | None = kwargs.pop('id')
        if 'name' in kwargs:
            self.name: str | None = kwargs.pop('name')
        if 'min_size' in kwargs:
            self.min_size: float | None = kwargs.pop('min_size')
        super().__init__(**kwargs)


class CryptoCurrenciesResponse(BaseResponse):
    """
        [
        {
            "code": "BTC",
            "name": "Bitcoin",
            "color": "#F7931A",
            "sort_index": 100,
            "exponent": 8,
            "type": "crypto",
            "address_regex": "^([13][a-km-zA-HJ-NP-Z1-9]{25,34})|^(bc1[qzry9x8gf2tvdw0s3jn54khce6mua7l]([qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}|[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{58}))$",
            "asset_id": "5b71fc48-3dd3-540c-809b-f8c94d0e68b5"
        },
        {
            "code": "ETH",
            "name": "Ethereum",
            "color": "#627EEA",
            "sort_index": 102,
            "exponent": 8,
            "type": "crypto",
            "address_regex": "^(?:0x)?[0-9a-fA-F]{40}$",
            "asset_id": "d85dce9b-5b73-5c3c-8978-522ce1d1c1b4"
        },
        {
            "code": "ETH2",
            "name": "Ethereum 2",
            "color": "#8E76FF",
            "sort_index": 161,
            "exponent": 8,
            "type": "crypto",
            "address_regex": "^(?:0x)?[0-9a-fA-F]{40}$",
            "asset_id": "3bec5bf3-507a-51ba-8e41-dc953b1a5c4d"
        },
        {
            "code": "ETC",
            "name": "Ethereum Classic",
            "color": "#59D4AF",
            "sort_index": 103,
            "exponent": 8,
            "type": "crypto",
            "address_regex": "^(?:0x)?[0-9a-fA-F]{40}$",
            "asset_id": "c16df856-0345-5358-8a70-2a78c804e61f"
        }
        ]
    """
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: list[CryptoCurrency] | None = [
                CryptoCurrency(**cc) for cc in response.pop('data')
            ]
        super().__init__(**response) 



class CryptoCurrency(BaseResponse):
    def __init__(self, **kwargs):
        if 'code' in kwargs:
            self.code: str | None = kwargs.pop('code')

        if 'name' in kwargs:
            self.name: str | None = kwargs.pop('name')

        if 'color' in kwargs:
            self.color: str | None = kwargs.pop('color')

        if 'sort_index' in kwargs:
            self.sort_index: str | None = kwargs.pop('sort_index')

        if 'exponent' in kwargs:
            self.exponent: str | None = kwargs.pop('exponent')

        if 'type' in kwargs:
            self.type: str | None = kwargs.pop('type')

        if 'address_regex' in kwargs:
            self.address_regex: str | None = kwargs.pop('address_regex')

        if 'asset_id' in kwargs:
            self.asset_id: str | None = kwargs.pop('asset_id')
        super().__init__(**kwargs)