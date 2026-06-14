# trade_manager.py

def execute_trade(signal):
    """
    Handle trading signals.
    """

    if signal == "BUY":
        print("BUY signal detected")

    elif signal == "SELL":
        print("SELL signal detected")

    else:
        print("Waiting for a trading opportunity")