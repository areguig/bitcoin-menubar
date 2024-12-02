#!/usr/bin/env python3
import rumps
import requests
import time
from datetime import datetime
import json
import os

class BitcoinPriceApp(rumps.App):
    def __init__(self):
        super(BitcoinPriceApp, self).__init__("BTC")
        self.config_file = os.path.expanduser('~/.bitcoin_price_config.json')
        self.load_config()
        self.last_price = None
        self.menu = [
            "Refresh",
            None,  # Separator
            rumps.MenuItem("Preferences", [
                "Refresh Interval",
                "Reset Preferences"
            ]),
            "About"
        ]
        self.update_price(None)  # Initial price update
        self.timer = rumps.Timer(self.update_price, self.config['refresh_interval'])
        self.timer.start()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.config = {'refresh_interval': 60}
            self.save_config()

    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f)
        except Exception as e:
            rumps.alert("Error", f"Failed to save config: {str(e)}")

    def format_price(self, price):
        return "${:,.2f}".format(float(price))

    def get_percent_change(self, current_price):
        if self.last_price is None:
            return ""
        percent = ((float(current_price) - float(self.last_price)) / float(self.last_price)) * 100
        if percent < 0:
            return f" ↓ ({percent:+.2f}%)"
        return f" ({percent:+.2f}%)"

    def update_price(self, _):
        try:
            response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot", timeout=10)
            response.raise_for_status()
            data = response.json()
            current_price = data['data']['amount']
            
            # Format the price with commas and two decimal places
            formatted_price = self.format_price(current_price)
            
            # Add percent change if we have a last price
            if self.last_price:
                percent_change = self.get_percent_change(current_price)
                self.title = f"{formatted_price}{percent_change}"
            else:
                self.title = formatted_price
                
            self.last_price = current_price
            
        except requests.RequestException as e:
            self.title = "Error"
            rumps.notification(
                title="Bitcoin Price Error",
                subtitle="Failed to fetch price",
                message=str(e)
            )
        except Exception as e:
            self.title = "Error"
            rumps.notification(
                title="Bitcoin Price Error",
                subtitle="Unexpected error",
                message=str(e)
            )

    @rumps.clicked("Refresh")
    def refresh(self, _):
        self.update_price(None)

    @rumps.clicked("Preferences", "Refresh Interval")
    def set_refresh_interval(self, _):
        try:
            response = rumps.Window(
                message="Enter refresh interval in seconds (minimum 10):",
                default_text=str(self.config['refresh_interval']),
                dimensions=(100, 20)
            ).run()
            
            if response.clicked:
                interval = int(response.text)
                if interval < 10:
                    rumps.alert("Error", "Minimum refresh interval is 10 seconds")
                    return
                
                self.config['refresh_interval'] = interval
                self.save_config()
            
                # Update the timer
                self.timer.stop()
                self.timer = rumps.Timer(self.update_price, interval)
                self.timer.start()
            
        except ValueError:
            rumps.alert("Error", "Please enter a valid number")

    @rumps.clicked("Preferences", "Reset Preferences")
    def reset_preferences(self, _):
        self.config = {'refresh_interval': 60}
        self.save_config()
        self.timer.stop()
        self.timer = rumps.Timer(self.update_price, 60)
        self.timer.start()
        rumps.alert("Preferences Reset", "Settings have been restored to defaults")

    @rumps.clicked("About")
    def about(self, _):
        rumps.alert(
            title="About Bitcoin Price",
            message="A simple menu bar app to track Bitcoin price.\n\n"
                   "Data provided by Coinbase API\n"
                   "GitHub: https://github.com/areguig/bitcoin-menubar"
        )

if __name__ == "__main__":
    app = BitcoinPriceApp()
    app.run()
