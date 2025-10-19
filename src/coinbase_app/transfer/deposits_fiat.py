from typing import Any 
from coinbase_app.constants import API_PREFIX

from coinbase_app.types.transfer_types import DepositFundsResponse
from coinbase_app.types.transfer_types import CommitDepositResponse
from coinbase_app.types.transfer_types import ListDepositsResponse
from coinbase_app.types.transfer_types import ShowDepositResonse

DOC = """
The Deposit resource represents a deposit of funds using a payment method (e.g., a bank). Each committed deposit also has an associated transaction.
You can start a withdrawal with the flag, commit: false, which is useful if you want to display a deposit before executing. Deposits made with commit set to false will not complete nor receive an associated transaction until a separate commit request is made.

Parameter	
    Description
id string	
    Resource ID
status string, enumerable	
    Status of the deposit. Valid values: created, completed, canceled
payment_method hash	
    Associated payment method (e.g., a bank)
transaction hash	
    Associated transaction (e.g., a bank, fiat account)
amount money hash
    Amount
subtotal money hash	
    Amount without fees
fee money hash	
    Fees associated to this deposit
created_at timestamp	
updated_at timestamp	
resource string, constant deposit	
resource_path string	
committed boolean	
    Has this deposit been committed?
payout_at timestamp, optional	
    When a deposit isn't executed instantly, it receives a payout date for the time it will be executed
"""


def deposit_funds(
        self, 
        account_id: str,
        amount: str,
        currency: str,
        payment_method: str,
        commit: bool | None,
        **kwargs) -> DepositFundsResponse:
    """
    Deposits user-defined amount of funds to a fiat account.
    ​
    ## Arguments
    Parameter	Type	Required	Description
    ==========
    amount	        string	Required	Deposit amount
    currency	    string	Required	Currency for the amount
    payment_method	string	Required	ID of payment method to be used for the deposit. List Payment Methods: GET /payment-methods
    commit	        boolean	Optional	If false, this deposit is not immediately completed. Use the commit call to complete it. Default value: false

    """
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/deposits"
    data = {
        'amount': amount,
        'currenccy': currency,
        'payment_method': payment_method,
        'commit': commit
    }
    return DepositFundsResponse(self.post(endpoint, data=data, **kwargs))

def commit_deposit(self, account_id: str, deposit_id: str, **kwargs) -> CommitDepositResponse:
    """
    Completes a deposit that is created in commit: false state.

    ## Arguments
        None

    """
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/deposits/{deposit_id}/commit"
    return CommitDepositResponse(self.post(endpoint, **kwargs))

def list_deposits(self, account_id: str, **kwargs):
    """
    Lists fiat deposits for an account.
    Deposits are only listed for fiat accounts and wallets. To list deposits associated with a crypto account/wallet, use List Transactions.
    
    ## Arguments
        None
    """
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/deposits"
    return ListDepositsResponse(self.get(endpoint, **kwargs))

def show_deposits(self, account_id: str, deposit_id: str, **kwargs):
    """
    Get one deposit by deposit Id.

    ## Arguments
        None
    """
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/deposits/{deposit_id}"
    return ShowDepositResonse(self.get(endpoint, **kwargs))






