from typing import Any 
from coinbase_app.constants import API_PREFIX

from coinbase_app.types.transfer_types import (
    CreateAddressResponse,
    ListAddressesResponse,
    ShowAddressResponse,
    ListTransactionsByAddressResponse
)

DOC = """
The Address resource represents an address for any Coinbase supported asset. An account can have more than one address, but an address can only be associated with one account.
To be notified when an address receives a new transactions, you can set up an API notification
"""

def create_address(self, account_id: str, name: str|None, **kwargs) -> CreateAddressResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}"
    data: dict[str,Any] = {
        'name': name
    }
    return CreateAddressResponse(self.post(endpoint, data, **kwargs))

def list_addresses(self, account_id: str, **kwargs):
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/addresses"
    return ListAddressesResponse(self.get(endpoint, **kwargs))

def show_address(self, account_id: str, address_id: str, **kwargs):
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/addresses/{address_id}"
    return ShowAddressResponse(self.get(endpoint, **kwargs))

def list_transactions_by_address(self, account_id: str, address_id: str, **kwargs) -> ListTransactionsByAddressResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/addresses/{address_id}/transactions"
    return ListTransactionsByAddressResponse(self.get(endpoint, **kwargs))