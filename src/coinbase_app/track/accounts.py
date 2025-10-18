"""
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
"""
from typing import Any

from coinbase_app.constants import API_PREFIX
from coinbase_app.types.account_types import ListAppAccountsResponse
from coinbase_app.types.account_types import ListAppAccountResponse 

def get_accounts(
    self,
    **kwargs
) -> ListAppAccountsResponse:
    endpoint = f"{API_PREFIX}/accounts"
    params: dict = {}
    return ListAppAccountsResponse(self.get(endpoint, params=params, **kwargs))


def get_account(
    self,
    account_id,
    **kwargs
) -> ListAppAccountResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}"
    return ListAppAccountResponse(self.get(endpoint, **kwargs))
