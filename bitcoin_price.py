#!/usr/bin/env python3
import rumps
import requests
import time
from datetime import datetime

class BitcoinPriceApp(rumps.App):
    def __init__(self):
        super(BitcoinPriceApp, self).__init__("BTC")
        self.menu = ["Refresh", "About"]
        self.update_price()
        
    def update_price(self):
        try:
            response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
            data = response.json()
            price = float(data["data"]["amount"])
            self.title = f"₿ ${price:,.0f}"
        except Exception as e:
            self.title = "₿ Error"
            
    @rumps.clicked("Refresh")
    def refresh(self, _):
        self.update_price()
        
    @rumps.clicked("About")
    def about(self, _):
        rumps.alert(title="About Bitcoin Price",
                   message="Simple Bitcoin price tracker using Coinbase API\nUpdates every minute")
        
    @rumps.timer(60)
    def update_timer(self, _):
        self.update_price()

if __name__ == "__main__":
    BitcoinPriceApp().run()
