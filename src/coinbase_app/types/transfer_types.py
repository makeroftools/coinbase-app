from typing import Any
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse



class DepositFundsResponse(BaseResponse):
    """
    """
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer: 

class CommitDepositResponse(BaseResponse):
    """
    """
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer = response.pop('transfer')


class ListDepositsResponse(BaseResponse):
    """
    """
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination = response.pop('pagination')
        if 'data' in response:
            self.data: list[Deposit] = [
                Deposit(**item) for item in response.pop('data')
            ]

class ShowDepositResonse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data = response.pop('data')

class WithdrawalFundsResponse(BaseResponse):
    def __int__(self, response: dict):
        if 'transfer' in response:
            self.transfer: dict[str,Any] = response.pop('transfer')

class CommitWithdrawalResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer: dict = response.pop('transfer')

class ListWithdrawalsResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination = response.pop('pagination')
        if 'data' in response:
            self.data: list[Withdrawal] = [
                Withdrawal(**w) for w in response.pop('data')
            ]

class ShowWithdrawalsResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict = response.pop('data')




strn = str | None

class Deposit(BaseResponse):
    """
    """
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id: strn = kwargs.pop('id')
        
        if 'status' in kwargs:
            self.status: strn = kwargs.pop('status')
        
        if 'payment_method' in kwargs:
            self.payment_method: strn = kwargs.pop('payment_method')

        if 'transaction' in kwargs:
            self.transaction: strn = kwargs.pop('transaction')

        if 'amount' in kwargs:
            self.amount: strn = kwargs.pop('amount')

        if 'subtotal' in kwargs:
            self.subtotal: strn = kwargs.pop('subtotal')

        if 'created_at' in kwargs:
            self.created_at: strn = kwargs.pop('created_at')

        if 'updated_at' in kwargs:
            self.updated_at: strn = kwargs.pop('updated_at')

        if 'resource' in kwargs:
            self.resource: strn = kwargs.pop('resource')

        if 'resource_path' in kwargs:
            self.resource_path: strn = kwargs.pop('resource_path')

        if 'committed' in kwargs:
            self.committed: strn = kwargs.pop('committed')

        if 'fee' in kwargs:
            self.fee: strn = kwargs.pop('fee')

        if 'payout_at' in kwargs:
            self.payout_at: strn = kwargs.pop('payout_at')

class Withdrawal(Deposit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)