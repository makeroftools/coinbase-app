from typing import Any
from coinbase_app.adv_trade.rest.types.base_response import BaseResponse



class DepositFundsResponse(BaseResponse):
    """
{
  {
    "transfer": {
        "user_entered_amount": {
            "value": "20",
            "currency": "USD"
        },
        "amount": {
            "value": "20",
            "currency": "USD"
        },
        "total": {
            "value": "20",
            "currency": "USD"
        },
        "subtotal": {
            "value": "20",
            "currency": "USD"
        },
        "idem": "7ada05f0-4ab9-4e42-8cb9-4501e795315d",
        "committed": false,
        "id": "7ada05f0-4ab9-4e42-8cb9-4501e795315d",
        "instant": true,
        "source": {
            "type": "EXTERNAL_PAYMENT_METHOD",
            "network": "ach",
            "payment_method_id": "",
            "external_payment_method": {
                "payment_method_id": "5a48fe239b15170130598e9c"
            }
        },
        "target": {
            "type": "LEDGER_ACCOUNT",
            "network": "internal_retail",
            "payment_method_id": "",
            "ledger_account": {
                "account_id": "6c770048-a3aa-580b-b153-2a6791649ee4",
                "currency": "USD",
                "owner": {
                    "id": "5a48fda3bbf66c03a6509af2",
                    "uuid": "",
                    "user_uuid": "",
                    "type": "RETAIL"
                }
            }
        },
        "payout_at": "2025-04-09T20:13:48.917581730Z",
        "status": "",
        "user_reference": "",
        "type": "TRANSFER_TYPE_DEPOSIT",
        "created_at": null,
        "updated_at": null,
        "user_warnings": [],
        "fees": [],
        "total_fee": {
            "title": "Fee Total",
            "description": "Total fee associated with this transaction",
            "amount": {
                "value": "0.00",
                "currency": "USD"
            },
            "type": "COINBASE"
        },
        "cancellation_reason": null,
        "hold_days": 0,
        "nextStep": null,
        "checkout_url": "",
        "requires_completion_step": false
    }
}

}
    """
    def __init__(self, response: dict):
        if 'transfer' in response:
            self.transfer: 

class CommitDepositResponse(BaseResponse):
    ...


class ListDepositsResponse(BaseResponse):
    ...

class ShowDepositResonse(BaseResponse):
    ...