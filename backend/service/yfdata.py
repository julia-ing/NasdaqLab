import yfinance as yf
from prophet import Prophet


def get_stock_data(q):
    data = yf.download(q,
                      start='2022-01-01',
                      end='2023-05-10')
    return data


def predict(q, days):
    data = get_stock_data(q)
    data.reset_index(inplace=True)
    train = data[['Date', 'Close']]
    train = train.rename(columns={"Date": "ds", "Close": "y"})
    model = Prophet()
    model.fit(train)
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast
