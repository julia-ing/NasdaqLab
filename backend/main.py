from typing import Optional
from utils.kafka.producer import MessageProducer
from utils.kafka.consumer import MessageConsumer
from service.yfdata import get_stock_data, predict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import schema
from service.register import create_user
from service.login import login


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data/{q}")  # example of q: TSLA
def get_data_from_yf(q: Optional[str] = None):
    return get_stock_data(q).to_dict('records')


@app.get("/predict/{q}/{days}")  # days you want prediction
def predict_future_days(q: Optional[str] = None, days: Optional[int] = 1):
    return predict(q, days)


@app.post("/register")
def register(request: schema.User):
    return create_user(request=request)


@app.post("/login")
def signin(request: schema.User):
    return login(request=request)


@app.get("/produce")
def kafkaProducer():
    broker = ["localhost:9092"]
    topic = "test"
    pd = MessageProducer(broker, topic)
    msg = {"name": "yewon", "status": "hungry"}
    res = pd.send_message(msg)
    return res


@app.get("/consume")
def kafkaConsumer():
    broker = ["localhost:9092"]
    topic = "test"
    cs = MessageConsumer(broker, topic)
    cs.receive_message()
