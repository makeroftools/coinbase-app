from typing import Any

from coinbase_app.adv_trade.rest.types.base_response import BaseResponse


class SendMoneyResponse(BaseResponse):
    """
        {
        "data": {
            "id": "3c04e35e-8e5a-5ff1-9155-00675db4ac02",
            "type": "send",
            "status": "pending",
            "amount": {
            "amount": "-0.10000000",
            "currency": "BTC"
            },
            "native_amount": {
            "amount": "-1.00",
            "currency": "USD"
            },
            "description": null,
            "created_at": "2015-01-31T20:49:02Z",
            "updated_at": "2015-03-31T17:25:29-07:00",
            "resource": "transaction",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/3c04e35e-8e5a-5ff1-9155-00675db4ac02",
            "network": {
            "status": "pending",
            },
            "to": {
            "resource": "bitcoin_address",
            "address": "1AUJ8z5RuHRTqD1eikyfUUetzGmdWLGkpT"
            }
        }
        }
    """
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: dict[str,Any] = response.pop('data')
        super().__init__(**response)

class ListTransactionsResponse(BaseResponse):
    """
        {
        "pagination": {
            "ending_before": null,
            "starting_after": null,
            "limit": 25,
            "order": "desc",
            "previous_uri": null,
            "next_uri": null
        },
        "data": [
            {
            "id": "4117f7d6-5694-5b36-bc8f-847509850ea4",
            "type": "buy",
            "status": "pending",
            "amount": {
                "amount": "486.34313725",
                "currency": "BTC"
            },
            "native_amount": {
                "amount": "4863.43",
                "currency": "USD"
            },
            "description": null,
            "created_at": "2015-03-26T23:44:08-07:00",
            "updated_at": "2015-03-26T23:44:08-07:00",
            "resource": "transaction",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/4117f7d6-5694-5b36-bc8f-847509850ea4",
            "details": {
                "title": "Bought bitcoin",
                "subtitle": "using Capital One Bank"
            }
            },
            {
            "id": "005e55d1-f23a-5d1e-80a4-72943682c055",
            "type": "request",
            "status": "pending",
            "amount": {
                "amount": "0.10000000",
                "currency": "BTC"
            },
            "native_amount": {
                "amount": "1.00",
                "currency": "USD"
            },
            "description": "",
            "created_at": "2015-03-24T18:32:35-07:00",
            "updated_at": "2015-01-31T20:49:02Z",
            "resource": "transaction",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/005e55d1-f23a-5d1e-80a4-72943682c055",
            "to": {
                "resource": "email",
                "email": "rb@coinbase.com"
            },
            "details": {
                "title": "Requested bitcoin",
                "subtitle": "from rb@coinbase.com"
            }
            },
            {
            "id": "ff01bbc6-c4ad-59e1-9601-e87b5b709458",
            "type": "transfer",
            "status": "completed",
            "amount": {
                "amount": "-5.00000000",
                "currency": "BTC"
            },
            "native_amount": {
                "amount": "-50.00",
                "currency": "USD"
            },
            "description": "",
            "created_at": "2015-03-12T15:51:38-07:00",
            "updated_at": "2015-01-31T20:49:02Z",
            "resource": "transaction",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/ff01bbc6-c4ad-59e1-9601-e87b5b709458",
            "to": {
                "id": "58542935-67b5-56e1-a3f9-42686e07fa40",
                "resource": "account",
                "resource_path": "/v2/accounts/58542935-67b5-56e1-a3f9-42686e07fa40"
            },
            "details": {
                "title": "Transferred bitcoin",
                "subtitle": "to Secondary Account"
            }
            },
            {
            "id": "57ffb4ae-0c59-5430-bcd3-3f98f797a66c",
            "type": "send",
            "status": "completed",
            "amount": {
                "amount": "-0.00100000",
                "currency": "BTC"
            },
            "native_amount": {
                "amount": "-0.01",
                "currency": "USD"
            },
            "description": null,
            "created_at": "2015-03-11T13:13:35-07:00",
            "updated_at": "2015-03-26T15:55:43-07:00",
            "resource": "transaction",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/57ffb4ae-0c59-5430-bcd3-3f98f797a66c",
            "network": {
                "status": "off_blockchain",
                "name": "bitcoin"
            },
            "to": {
                "id": "a6b4c2df-a62c-5d68-822a-dd4e2102e703",
                "resource": "user",
                "resource_path": "/v2/users/a6b4c2df-a62c-5d68-822a-dd4e2102e703"
            },
            "details": {
                "title": "Send bitcoin",
                "subtitle": "to User 2"
            }
            }
        ]
        }
    """
    def __init__(self, response: dict):
        if 'pagination' in response:
            self.pagination: dict[str,Any] = response.pop('pagination')
        if 'data' in response:
            self.data: list[TransactionSummary] = [
                TransactionSummary(**txsum) for txsum in response.pop('data')
            ]
        super().__init__(**response)

class ShowTransactionResponse(BaseResponse):
    """
        {
        "data": {
            "id": "57ffb4ae-0c59-5430-bcd3-3f98f797a66c",
            "type": "send",
            "status": "completed",
            "amount": {
            "amount": "-0.00100000",
            "currency": "BTC"
            },
            "native_amount": {
            "amount": "-0.01",
            "currency": "USD"
            },
            "description": null,
            "created_at": "2015-03-11T13:13:35-07:00",
            "updated_at": "2015-03-26T15:55:43-07:00",
            "resource": "transaction",
            "resource_path": "/v2/accounts/2bbf394c-193b-5b2a-9155-3b4732659ede/transactions/57ffb4ae-0c59-5430-bcd3-3f98f797a66c",
            "network": {
            "status": "off_blockchain",
            "name": "bitcoin"
            },
            "to": {
            "id": "a6b4c2df-a62c-5d68-822a-dd4e2102e703",
            "resource": "user",
            "resource_path": "/v2/users/a6b4c2df-a62c-5d68-822a-dd4e2102e703"
            },
            "details": {
            "title": "Send bitcoin",
            "subtitle": "to User 2"
            }
        }
        }
    """
    def __init__(self, response: dict):
        if 'data' in response:
            self.data: list[Transaction] | None = [
                Transaction(**tx) for tx in response.pop('data')
            ] 
        super().__init__(**response)


class Transaction(BaseResponse):
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
        if 'to' in kwargs:
            self.to = kwargs.pop('to')
        if 'details' in kwargs:
            self.details = kwargs.pop('details')
        super().__init__(**kwargs)