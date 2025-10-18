from .__version__ import __version__
from .adv_trade.constants import (
    BASE_URL,
    X_RATELIMIT_LIMIT,
    X_RATELIMIT_REMAINING,
    X_RATELIMIT_RESET,
    RATE_LIMIT_HEADERS
) 

API_PREFIX = "/v2"

USER_AGENT = f"coinbase-app-py/{__version__}"