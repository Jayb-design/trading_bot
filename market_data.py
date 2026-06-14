# market_data.py

prices = []


def add_price(price):
    """
    Store a new market price.
    """
    prices.append(price)

    # Keep only the latest 100 prices
    if len(prices) > 100:
        prices.pop(0)


def get_prices():
    """
    Return all stored prices.
    """
    return prices