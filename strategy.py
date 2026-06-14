# strategy.py

def moving_average(prices, period):
    """
    Calculate the moving average.
    """

    if len(prices) < period:
        return None

    return sum(prices[-period:]) / period


def get_signal(prices):
    """
    Generate BUY, SELL, or WAIT signal.
    """

    period = 20

    ma = moving_average(prices, period)

    if ma is None:
        return "WAIT"

    current_price = prices[-1]

    if current_price > ma:
        return "BUY"

    elif current_price < ma:
        return "SELL"

    else:
        return "WAIT"
    