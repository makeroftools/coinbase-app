
"""
# List Accounts Response
{
  "pagination": {
    "ending_before": null,
    "starting_after": null,
    "limit": 25,
    "order": "desc",
    "previous_uri": null,
    "next_uri": null
  },
  "data": [
    {
      "id": "58542935-67b5-56e1-a3f9-42686e07fa40",
      "name": "My Vault",
      "primary": false,
      "type": "vault",
      "currency" : {
         "address_regex" : "^([13][a-km-zA-HJ-NP-Z1-9]{25,34})|^(bc1[qzry9x8gf2tvdw0s3jn54khce6mua7l]([qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}|[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{58}))$",
         "asset_id" : "5b71fc48-3dd3-540c-809b-f8c94d0e68b5",
         "code" : "BTC",
         "color" : "#F7931A",
         "exponent" : 8,
         "name" : "Bitcoin",
         "slug" : "bitcoin",
         "sort_index" : 100,
         "type" : "crypto"
      }
      "balance": {
        "amount": "4.00000000",
        "currency": "BTC"
      },
      "created_at": "2024-01-31T20:49:02Z",
      "updated_at": "2024-01-31T20:49:02Z",
      "resource": "account",
      "resource_path": "/v2/accounts/58542935-67b5-56e1-a3f9-42686e07fa40",
      "ready": true
    },
    {
      "id": "2bbf394c-193b-5b2a-9155-3b4732659ede",
      "name": "My Wallet",
      "primary": true,
      "type": "wallet",
      "currency" : {
         "address_regex" : "^([13][a-km-zA-HJ-NP-Z1-9]{25,34})|^(bc1[qzry9x8gf2tvdw0s3jn54khce6mua7l]([qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}|[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{58}))$",
         "asset_id" : "5b71fc48-3dd3-540c-809b-f8c94d0e68b5",
         "code" : "BTC",
         "color" : "#F7931A",
         "exponent" : 8,
         "name" : "Bitcoin",
         "slug" : "bitcoin",
         "sort_index" : 100,
         "type" : "crypto"
      }
      "balance": {
        "amount": "39.59000000",
        "currency": "BTC"
      },
      "created_at": "2024-01-31T20:49:02Z",
      "updated_at": "2024-01-31T20:49:02Z",
      "resource": "account",
      "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede"
    }
  ]
}
"""
"""
# List Account Response
{
  "data": {
    "id": "2bbf394c-193b-5b2a-9155-3b4732659ede",
    "name": "My Wallet",
    "primary": true,
    "type": "wallet",
      "currency" : {
         "address_regex" : "^([13][a-km-zA-HJ-NP-Z1-9]{25,34})|^(bc1[qzry9x8gf2tvdw0s3jn54khce6mua7l]([qpzry9x8gf2tvdw0s3jn54khce6mua7l]{38}|[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{58}))$",
         "asset_id" : "5b71fc48-3dd3-540c-809b-f8c94d0e68b5",
         "code" : "BTC",
         "color" : "#F7931A",
         "exponent" : 8,
         "name" : "Bitcoin",
         "slug" : "bitcoin",
         "sort_index" : 100,
         "type" : "crypto"
      }
    "balance": {
      "amount": "39.59000000",
      "currency": "BTC"
    },
    "created_at": "2024-01-31T20:49:02Z",
    "updated_at": "2024-01-31T20:49:02Z",
    "resource": "account",
    "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede"
  }
}
"""
from typing import Any
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse


class AppAccountsResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination: dict[str,Any] = response.pop("pagination")
        if 'data' in response:
            self.accounts: list[AppAccount] = [
                AppAccount(**account) for account in response.pop("data")
            ]
        super().__init__(**response)

class AppAccountResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response)

class AppAccount(BaseResponse):
    def __init__(self, **kwargs):
        if 'id' in kwargs: 
            self.id: str | None = kwargs.pop('id')
        if 'name' in kwargs:
            self.name: str | None = kwargs.pop('id')
        if 'primary' in kwargs: 
            self.primary: bool | None = kwargs.pop('primary')
        if 'type' in kwargs:
            self.type: str | None = kwargs.pop('type')
        if 'currency' in kwargs:
            self.currency: dict[str,Any] | None = kwargs.pop('currency')
        if 'balance' in kwargs:
            self.balance: dict[str,Any] | None = kwargs.pop('balance')
        if 'created_at' in kwargs:
            self.created_at: str | None = kwargs.pop('created_at')
        if 'updated_at' in kwargs:
            self.updated_at: str | None = kwargs.pop('updated_at')

        if 'resource' in kwargs:
            self.resource: str | None = kwargs.pop('resource')
        if 'resource_path' in kwargs:
            self.resource_path: str | None = kwargs.pop('resource_path')
        if 'ready' in kwargs:
            self.ready: str | None = kwargs.pop('ready')
        super().__init__(**kwargs)
