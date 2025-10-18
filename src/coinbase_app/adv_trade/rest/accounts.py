"""
{
  "accounts": [
    {
      "uuid": "8bfc20d7-f7c6-4422-bf07-8243ca4169fe",
      "name": "BTC Wallet",
      "currency": "BTC",
      "available_balance": {
        "value": "1.23",
        "currency": "BTC"
      },
      "default": false,
      "active": true,
      "created_at": "2021-05-31T09:59:59.000Z",
      "updated_at": "2021-05-31T09:59:59.000Z",
      "deleted_at": "2021-05-31T09:59:59.000Z",
      "type": "FIAT",
      "ready": true,
      "hold": {
        "value": "1.23",
        "currency": "BTC"
      },
      "retail_portfolio_id": "b87a2d3f-8a1e-49b3-a4ea-402d8c389aca",
      "platform": "ACCOUNT_PLATFORM_CONSUMER"
    }
  ],
  "has_next": true,
  "cursor": "789100",
  "size": 123
}
"""
from typing import Any, Dict, Optional

from adv_trade.constants import API_PREFIX
from adv_trade.rest.types.accounts_types import GetAccountResponse, ListAccountsResponse


def get_accounts(
    self,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    retail_portfolio_id: Optional[str] = None,
    **kwargs,
) -> ListAccountsResponse:
    """
    **List Accounts**
    _________________
    [GET] https://api.coinbase.com/api/v3/brokerage/accounts

    __________

    **Description:**

    Get a list of authenticated accounts for the current user.

    __________

    **Read more on the official documentation:** `List Accounts <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getaccounts>`_

    """
    endpoint = f"{API_PREFIX}/accounts"
    params = {
        "limit": limit,
        "cursor": cursor,
        "retail_portfolio_id": retail_portfolio_id,
    }

    return ListAccountsResponse(self.get(endpoint, params=params, **kwargs))


def get_account(self, account_uuid: str, **kwargs) -> GetAccountResponse:
    """

    **Get Account**
    _______________
    [GET] https://api.coinbase.com/api/v3/brokerage/accounts/{account_uuid}

    __________

    **Description:**

    Get a list of information about an account, given an account UUID.

    __________

    **Read more on the official documentation:** `Get Account <https://docs.cdp.coinbase.com/advanced-trade/reference/retailbrokerageapi_getaccount>`_
    """
    endpoint = f"{API_PREFIX}/accounts/{account_uuid}"

    return GetAccountResponse(self.get(endpoint, **kwargs))
