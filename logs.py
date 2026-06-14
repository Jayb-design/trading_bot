# trade_manager.py

from datetime import datetime


def log_trade(message):
    with open("logs/trades.log", "a") as file:
        file.write(message + "\n")


def execute_trade(signal):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if signal == "BUY":

        message = f"{current_time} | BUY signal detected"

        print(message)
        log_trade(message)

    elif signal == "SELL":

        message = f"{current_time} | SELL signal detected"

        print(message)
        log_trade(message)

    else:

        message = f"{current_time} | WAIT"

        print(message)
        log_trade(message)