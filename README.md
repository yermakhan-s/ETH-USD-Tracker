ETHTrack Documentation
======================

The ETHTrack class is designed to track the prices of Ethereum (ETH) and Bitcoin (BTC) in USD using the Coinbase API. It calculates the correlation between the historical prices of ETH and BTC, and provides summaries of the price changes over a specific time interval.

Dependencies:
--------------
The code relies on the following external libraries:
- time
- datetime from datetime module
- sleep from time module
- requests
- numpy

Class:
------
ETHTrack:
    A class that tracks the prices of Ethereum (ETH) and Bitcoin (BTC) in USD and provides summaries of the price changes.

    Methods:
    --------
    __init__():
        Constructor method that initializes the ETHTrack object.
        - eth_history: A list to store the historical prices of ETH.
        - btc_history: A list to store the historical prices of BTC.
        - correlation_threshold: A threshold value used to determine if the correlation coefficient is significant.

    calculate_correlation():
        Calculates the correlation coefficient between the historical prices of ETH and BTC.
        - Returns: The correlation coefficient as a float value.

    get_price():
        Fetches the current prices of ETH and BTC from the Coinbase API and appends them to the respective history lists.

    calculate_change(eth, btc, prev_eth, prev_btc):
        Calculates the percentage change in the prices of ETH and BTC between two given points in time.
        - eth: Current price of ETH as a float.
        - btc: Current price of BTC as a float.
        - prev_eth: Previous price of ETH as a float.
        - prev_btc: Previous price of BTC as a float.
        - Returns: A list containing the percentage changes in ETH and BTC prices.

    print_eth():
        Prints the current price of ETH/USD along with the percentage change in prices compared to the previous value.

    results():
        Prints a summary of the price changes and the correlation coefficient between ETH and BTC.
        - If the correlation coefficient is below the threshold and the percentage change in ETH price is above 1.00%, an "ATTENTION!!!" message is displayed.
        - Otherwise, the 60-second summary of price changes and the correlation coefficient are printed.

    start():
        Initiates the tracking process by fetching prices at regular intervals for 60 seconds.
        - Prints the results summary after each interval.
        - Clears the price history lists at the end of each interval.

Usage:
------
To use the ETHTrack class, perform the following steps:
1. Import the necessary modules and libraries.
2. Create an instance of the ETHTrack class.
3. Call the `start()` method to begin the tracking process.

Example:
--------
import time
from datetime import datetime
from time import sleep
import requests
import numpy as np

class ETHTrack:
    # Code implementation here...

if __name__ == '__main__':
    module = ETHTrack()
    module.start()
