import time
from datetime import datetime
from time import sleep
import requests
import numpy as np

class ETHTrack:
    def __init__(self):
        self.eth_history = []
        self.btc_history = []
        self.correlation_threshold = 0.8

    def calculate_correlation(self):
        x = np.array(self.eth_history)
        y = np.array(self.btc_history)
        cor_coef = np.corrcoef(x, y)
        return cor_coef[0][1]

    def get_price(self):
        eth_url = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'
        btc_url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

        eth_response = requests.get(eth_url)
        eth_data = eth_response.json()

        btc_response = requests.get(btc_url)
        btc_data = btc_response.json()

        self.eth_history.append(float(eth_data['data']['amount']))
        self.btc_history.append(float(btc_data['data']['amount']))

    def calculate_change(self, eth, btc, prev_eth, prev_btc):
        eth_change = (eth/prev_eth-1)*100
        btc_change = (btc/prev_btc-1)*100
        return [eth_change, btc_change]

    def print_changes(self):
        if len(self.eth_history) >= 2:
            changes = self.calculate_change(self.eth_history[-1], self.btc_history[-1],
                                                 self.eth_history[-2], self.btc_history[-2])
        else:
            changes = [0.00, 0.00]
        print(f"ETH/USD: ${self.eth_history[-1]:.2f} [{changes[0]:.2f}%] BTC/USD: ${self.btc_history[-1]:.2f} [{changes[1]:.2f}%]")

    def results(self):
        cor_coef = abs(self.calculate_correlation())
        change_in_minute = self.calculate_change(self.eth_history[-1], self.btc_history[-1],
                                                 self.eth_history[0], self.btc_history[0])
        print("-------------------------------------------------------------------------------------------")
        if cor_coef < self.correlation_threshold and change_in_minute[0] >= 1.00:
            print(f"ATTENTION!!! ETH/USD has a independent significant change of {change_in_minute[0]:.2f}%")
        else:
            print(f"60 seconds summary: ETH/USD: [{change_in_minute[0]:.2f}%] BTC/USD: [{change_in_minute[1]:.2f}%]")
            print(f"correlation coefficient: [{cor_coef:.2f}]")
        print(f"Time: [{datetime.now()}]")
        print("-------------------------------------------------------------------------------------------")

    def start(self):
        while True:
            t_end = time.time() + 60
            while time.time() < t_end:
                self.get_price()
                self.print_changes()
                sleep(1)
            self.results()
            self.eth_history.clear()
            self.btc_history.clear()

if __name__ == '__main__':
    module = ETHTrack()
    module.start()
