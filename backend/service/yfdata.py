import yfinance as yf


def get_stock_data(q):
    data = yf.download(q,
                      start='2022-01-01',
                      end='2023-05-10')  # TODO: change
    return data
