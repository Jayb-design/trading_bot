# trade_manager.py

import websocket
import json

from market_data import get_prices
from config import SYMBOL


def execute_trade(signal):
    """
    Execute a trade based on the signal.
    """

    if signal == "BUY":
        buy()

    elif signal == "SELL":
        sell()