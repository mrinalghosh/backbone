from dataclasses import dataclass
from datetime import datetime
import pandas as pd
from datetime import datetime
import yfinance as yf

@dataclass
class StockData:
    ''' Class for stock data from Yahoo Finance '''
    def __init__(self, ticker: str, start, end) -> None:
        self.ticker = ticker
        self.df = yf.download(ticker, start, end)
        # use date-time range to decide whether to update class
        self.start = start
        self.end = end

class Portfolio:
    def __init__(self) -> None:
        self.df = None


if __name__ == '__main__':
    pass