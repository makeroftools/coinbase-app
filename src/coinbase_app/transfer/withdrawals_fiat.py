from typing import Any 
from coinbase_app.constants import API_PREFIX

from coinbase_app.types.transfer_types import (
    WithdrawalFundsResponse,
    CommitWithdrawalResponse,
    ListWithdrawalsResponse,
    ShowWithdrawalsResponse
)

DOC = """
The Withdrawal resource represents a withdrawal of funds using a payment method 
(e.g., a bank). Each committed withdrawal also has an associated transaction.

NOTE: 
    You can start a withdrawal with the flag, commit: false, which is useful if you 
    want to display a withdrawal before executing. Withdrawals made with commit set 
    to false will not complete nor receive an associated transaction until a 
    separate commit request is made.

"""

def withdrawal_funds(self, account_id: str, **kwargs) -> WithdrawalFundsResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/withdrawals"
    return WithdrawalFundsResponse(self.post(endpoint, **kwargs))

def commit_withdrawal(self, account_id: str, withdrawal_id: str, **kwargs) -> CommitWithdrawalResponse
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/withdrawals/{withdrawal_id}/commit"
    return CommitWithdrawalResponse(self.post(endpoint, **kwargs))

def list_withdrawals(self, account_id: str, **kwargs) -> ListWithdrawalsResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/withdrawals"
    return ListWithdrawalsResponse(self.get(endpoint, **kwargs))

def show_withdrawal(self, account_id: str, withdrawal_id: str, **kwargs) -> ShowWithdrawalsResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/withdrawals/{withdrawal_id}"
    return ShowWithdrawalsResponse(self.get(endpoint, **kwargs))