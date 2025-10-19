from adv_trade.rest.rest_base import RESTBase


class AppClient(RESTBase):
    """
    """
    from .track.accounts import (
        get_account,
        get_accounts
    )
    from .track.currencies import (
        get_fiat_currencies,
        get_crypto_currencies
    )
    from .track.transactions import (
        send_money,
        list_transactions,
        show_transaction
    )
    from .transfer.deposits_fiat import (
        deposit_funds,
        commit_deposit,
        list_deposits,
        show_deposits
    )
    from .transfer.withdrawals_fiat import (
        withdrawal_funds,
        commit_withdrawal,
        list_withdrawals,
        show_withdrawal
    )