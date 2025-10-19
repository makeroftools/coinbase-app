from typing import Any
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse



class DepositFundsResponse(BaseResponse):
    """
    """
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer: 
        super().__init__(**response)
class CommitDepositResponse(BaseResponse):
    """
    """
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer = response.pop('transfer')
        super().__init__(**response)

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
        super().__init__(**response)
class ShowDepositResonse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data = response.pop('data')
        super().__init__(**response)
class WithdrawalFundsResponse(BaseResponse):
    def __int__(self, response: dict):
        if 'transfer' in response:
            self.transfer: dict[str,Any] = response.pop('transfer')
        super().__init__(**response)
class CommitWithdrawalResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer: dict = response.pop('transfer')
        super().__init__(**response)
class ListWithdrawalsResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination = response.pop('pagination')
        if 'data' in response:
            self.data: list[Withdrawal] = [
                Withdrawal(**w) for w in response.pop('data')
            ]
        super().__init__(**response)
class ShowWithdrawalsResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict = response.pop('data')
        super().__init__(**response)
class CreateAddressResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data = response.pop('data')
        super().__init__(**response)

class ListAddressesResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination = response.pop('pagination')
        if 'data' in response:
            self.data: list[Address] = [
                Address(**a) for a in response.pop('data')
            ]
        super().__init__(**response)

class ShowAddressResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response)

class ListTransactionsByAddressResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination: dict[str,Any] = response.pop('pagination')
        if 'data' in response:
            self.data: list[TransactionByAddress] = [
                TransactionByAddress(*tx) for tx in response.pop('data')
            ]
        super().__init__(**response)


class SendCryptoResponse(BaseResponse):
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response))

###########
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
        super().__init__(**kwargs)
class Withdrawal(Deposit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Address(BaseResponse):
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs.pop('id')
        if 'address' in kwargs:
            self.address = kwargs.pop('address')
        if 'name' in kwargs:
            self.name = kwargs.pop('name')
        if 'created_at' in kwargs:
            self.created_at = kwargs.pop('created_at')
        if 'updated_at' in kwargs:
            self.updated_at = kwargs.pop('updated_at')
        if 'network' in kwargs:
            self.network = kwargs.pop('network')
        if 'resource' in kwargs:
            self.resource = kwargs.pop('resource')
        if 'resource_path' in kwargs:
            self.resource_path = kwargs.pop('resource_path')
        super().__init__(**kwargs)

class TransactionByAddress(BaseResponse):
    def __init__(self, **kwargs):
        if 'id' in kwargs:
            self.id = kwargs.pop('id')
        if 'type' in kwargs:
            self.type = kwargs.pop('type')
        if 'status' in kwargs:
            self.status = kwargs.pop('status')
        if 'amount' in kwargs:
            self.amount = kwargs.pop('amount')
        if 'native_amount' in kwargs:
            self.native_amount = kwargs.pop('native_amount')
        if 'description' in kwargs:
            self.description = kwargs.pop('description')
        if 'created_at' in kwargs:
            self.created_at = kwargs.pop('created_at')
        if 'updated_at' in kwargs:
            self.updated_at = kwargs.pop('updated_at')
        if 'resource' in kwargs:
            self.resource = kwargs.pop('resource')
        if 'resource_path' in kwargs:
            self.resource_path = kwargs.pop('resource_path')
        if 'network' in kwargs:
            self.network = kwargs.pop('network')
        if 'from' in kwargs:
            self.from_ = kwargs.pop('from')
        super().__init__(**kwargs)