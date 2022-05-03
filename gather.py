import yfinance as yf
import pandas as pd

def save(df, file='./data/tmp.pkl') -> None:
    ''' pickle data for storage and later retrieval'''
    df.to_pickle(file)

def load(file='./data/cached.pkl') -> pd.DataFrame:
    ''' load pickled data '''
    return pd.read_pickle(file)

if __name__ == '__main__':
    tickers = ['MSFT', 'SPY']
    df = yf.download(tickers, start='2020-01-01', end='2020-12-31')
    # save(df)

    # df = load()

    print(df)