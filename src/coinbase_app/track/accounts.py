from typing import Any

from coinbase_app.constants import API_PREFIX
from coinbase_app.types.account_types import AppAccountsResponse
from coinbase_app.types.account_types import AppAccountResponse 

def get_accounts(
    self,
    **kwargs
) -> AppAccountsResponse:
    endpoint = f"{API_PREFIX}/accounts"
    params: dict = {}
    return AppAccountsResponse(self.get(endpoint, params=params, **kwargs))


def get_account(
    self,
    account_id,
    **kwargs
) -> AppAccountResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}"
    return AppAccountResponse(self.get(endpoint, **kwargs))
