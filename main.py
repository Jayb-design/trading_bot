import websocket
import json

from market_data import add_price, get_prices
from strategy import get_signal
from trade_manager import execute_trade
from config import SYMBOL


def on_message(ws, message):
    """
    Called whenever Deriv sends a new price.
    """

    data = json.loads(message)

    if "tick" in data:

        # Extract current price
        price = float(data["tick"]["quote"])

        # Save price to our list
        add_price(price)

        # Get all stored prices
        prices = get_prices()

        # Generate trading signal
        signal = get_signal(prices)

        print("-" * 40)
        print("Current Price:", price)
        print("Signal:", signal)
        print("Prices Stored:", len(prices))

        # Execute trade logic
        execute_trade(signal)


def on_open(ws):
    """
    Called when connection is established.
    """

    print("Connected to Deriv")

    request = {
        "ticks": SYMBOL
    }

    ws.send(json.dumps(request))

    print("Subscribed to", SYMBOL)


def on_error(ws, error):
    print("Error:", error)


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


print("Starting Trading Bot...")

ws = websocket.WebSocketApp(
    "wss://ws.derivws.com/websockets/v3?app_id=1089",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever()