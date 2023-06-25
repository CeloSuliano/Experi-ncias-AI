import iqoptionapi
import time

def login():
    api = iqoptionapi.create("YOUR_API_KEY")
    return api.login("YOUR_USERNAME", "YOUR_PASSWORD")

def place_trade(symbol, type, amount, expiry, strike):
    api = login()
    trade = api.create_trade(symbol, type, amount, expiry, strike)
    return trade

def close_trade(trade_id):
    api = login()
    api.close_trade(trade_id)

def manage_risk(amount, risk):
    if amount * risk > 100:
        print("Too much risk!")
    else:
        print("Risk is acceptable.")

def monitor_account_performance():
    api = login()
    account_info = api.get_account_info()
    print("Account balance: " + account_info["balance"])
    print("Profit/loss: " + account_info["profitLoss"])

def monitor_assets():
    api = login()
    assets = api.get_assets()
    for asset in assets:
        print(asset["symbol"] + ": " + asset["lastPrice"])
        print("Probability of successful trade: " + asset["probability"])

def main():
    login()
    place_trade("EURUSD", "CALL", 100, "1m", 1.1150)
    close_trade(123456)
    manage_risk(100, 0.1)
    monitor_account_performance()
    monitor_assets()

if __name__ == "__main__":
    main()
