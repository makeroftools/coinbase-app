from typing import Any

from coinbase_app.constants import API_PREFIX
from coinbase_app.types.transaction_types import SendMoneyResponse
from coinbase_app.types.transaction_types import TransactionResponse
from coinbase_app.types.transaction_types import TransactionsResponse


def send_money(
    self,
    account_id: str,
    type: str,
    to: str,
    amount: str,
    currency: str,
    description: str | None,
    skip_notifications: bool | None,
    idem: str | None,
    destination_tag: str | None,
    network: str | None,
    travel_rule_data: dict[str,Any] | None,
    **kwargs
) -> SendMoneyResponse:
    endpoint = f"{API_PREFIX}/accounts/{account_id}/transactions"

    params = {
        'type': type,
        'to': to,
        'amount': amount,
        'currency': currency,
        'description': description,
        'skip_notifications': skip_notifications,
        'idem': idem,
        'destination_tag': destination_tag,
        'network': network,
        'travel_rule_data': travel_rule_data
    }

    return SendMoneyResponse(self.post(endpoint, params=params, **kwargs))

def get_transactions(
    self,
    account_id: str,
    **kwargs
) -> TransactionsResponse:
    endpoint = f"{API_PREFIX}/accounts/{account_id}/transations"
    return TransactionsResponse(self.get(endpoint, **kwargs))

def get_transaction(
    self,
    account_id: str,
    transaction_id: str,
    **kwargs
) -> TransactionResponse:
    endpoint = f"{API_PREFIX}/accounts/{account_id}/transactions/{transaction_id}"
    return TransactionResponse(self.get(endpoint, **kwargs))