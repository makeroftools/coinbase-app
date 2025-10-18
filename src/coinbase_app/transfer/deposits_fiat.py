from typing import Any 
from coinbase_app.constants import API_PREFIX

from coinbase_app.types.transfer_types import DepositFundsResponse
from coinbase_app.types.transfer_types import CommitDepositResponse
from coinbase_app.types.transfer_types import ListDepositsResponse
from coinbase_app.types.transfer_types import ShowDepositResonse



def deposit_funds(
        self, 
        account_id: str,
        amount: str,
        currency: str,
        payment_method: str,
        commit: bool | None,
        **kwargs) -> DepositFundsResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/deposits"
    data = {
        'amount': amount,
        'currenccy': currency,
        'payment_method': payment_method,
        'commit': commit
    }
    return DepositFundsResponse(self.post(endpoint, data=data, **kwargs))

def commit_deposit():
    ...

def list_deposits():
    ...

def show_deposits():
    ...






