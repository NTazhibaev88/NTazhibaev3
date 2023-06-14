import requests

class CryptoTrader:
    def __init__(self):
        self.api_url = "https://api.coingecko.com/api/v3"
        self.currencies = []

    def add_currency(self, currency):
        self.currencies.append(currency)

    def check_prices(self):
        print("Checking cryptocurrency prices...")
        for currency in self.currencies:
            response = requests.get(f"{self.api_url}/simple/price?ids={currency}&vs_currencies=usd")
            if response.status_code == 200:
                price_data = response.json()
                price = price_data[currency]["usd"]
                print(f"{currency}: ${price}")
            else:
                print(f"Failed to fetch price data for {currency}.")
        print("Price check complete.")

def main():
    trader = CryptoTrader()

    # Add cryptocurrencies to monitor
    trader.add_currency("bitcoin")
    trader.add_currency("ethereum")
    trader.add_currency("litecoin")

    # Check cryptocurrency prices
    trader.check_prices()

if __name__ == "__main__":
    main()
