from typing import Optional
from service.yfdata import get_stock_data, predict
from fastapi import FastAPI

app = FastAPI()

@app.get("/data/{q}")  # example of q: TSLA
def get_data_from_yf(q: Optional[str] = None):
    return get_stock_data(q).to_dict('records')

@app.get("/predict/{q}/{days}")  # days you want prediction
def predict_future_days(q: Optional[str] = None, days: Optional[int] = 1):
    return predict(q, days)
