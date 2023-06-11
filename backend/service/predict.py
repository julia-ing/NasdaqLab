from utils.kafka.producer import MessageProducer
from prophet import Prophet
from service.yfdata import get_stock_data


def predict(request, current_user):
    data = get_stock_data(request.stock)
    data.reset_index(inplace=True)
    train = data[['Date', 'Close']]
    train = train.rename(columns={"Date": "ds", "Close": "y"})
    model = Prophet()
    model.fit(train)
    future = model.make_future_dataframe(periods=request.days)
    forecast = model.predict(future)
    predicted_data = forecast['yhat'][-request.days:]
    average = sum(predicted_data) / len(predicted_data)

    broker = ["localhost:9092"]
    topic = "test2"
    pd = MessageProducer(broker, topic)
    msg = {"name": current_user.nickname, "stock": request.stock, "days": request.days, "predicted_val": average}
    pd.send_message(msg)

    return msg
