import yfinance as yf
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt


def save(df, file='./data/tmp.pkl') -> None:
    ''' pickle data for storage and later retrieval'''
    # make directory with datetime as name
    # save pickled finance data and metadata file with stocks, start-end, ...?
    df.to_pickle(file)


def load(file='./data/tmp.pkl') -> pd.DataFrame:
    ''' load pickled data '''
    return pd.read_pickle(file)


def plot(df: pd.DataFrame):
    df.plot()
    plt.show()

if __name__ == '__main__':
    # tickers = ['MSFT', 'SPY', 'PLTR']
    A : pd.DataFrame = yf.download(['PLTR'], start='2021-01-01', end='2021-01-31')
    B = yf.download(['SPY'], start='2021-01-01', end='2021-01-31')
    C = yf.download(['PLTR', 'AMD'], start='2021-01-01', end='2021-01-31')

    # micolumns = pd.MultiIndex.from_product([B, ['SPY']])
    # print(micolumns) 

    # print(A.columns)
    # A_ = pd.MultiIndex.from_frame(A, names=A.columns)
    # B_ = pd.MultiIndex.from_frame(B, names=[(b, 'SPY') for b in B.columns])
    B_ = pd.DataFrame(B, index=B.index, columns=[(b, 'SPY') for b in B.columns])
    print(B_)

    # print(pd.concat([A,B],keys=['SPY', 'PLTR'])) # B overwrites A

    print(C)

    # for stock in df.columns.get_level_values(1).unique():
    #     print(stock)

    # percent change graph - note the MultiIndex
    # plot((1+df['Adj Close'].pct_change()).cumprod())
    # plot(df)

    # save(df)
    # df = load()

    # print(df)
    # print(date.today())
