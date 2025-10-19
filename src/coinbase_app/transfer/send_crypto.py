from typing import Any 
from coinbase_app.constants import API_PREFIX

from coinbase_app.types.transfer_types import SendCryptoResponse


def send_crypto(
    self,
    account_id: str,
    type: str,
    to: str,
    amount: str,
    currency: str,
    description: str | None,
    skip_notifications: bool | None,
    idem: str | None,
    destination_flag: str | None,
    network: str | None,
    travel_rule_data: str | None,
    **kwargs
) -> SendCryptoResponse:
    endpoint: str = f"{API_PREFIX}/accounts/{account_id}/transactions"
    data: dict[str,Any] = {
        'type': type,
        'to': to,
        'amount': amount,
        'currency': currency,
        'description': description,
        'skip_notifications': skip_notifications,
        'idem': idem,
        'destination_flag': destination_flag,
        'network': network,
        'travel_rule_data': travel_rule_data
    }
    return SendCryptoResponse(self.post(endpoint, data=data, **kwargs))