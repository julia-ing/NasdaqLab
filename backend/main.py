from db.schema import Predict, User
from utils.jwt import get_current_user
from utils.kafka.producer import MessageProducer
from utils.kafka.consumer import MessageConsumer
from service.login import login
from service.predict import predict
from service.register import create_user
from service.yfdata import get_stock_data

from asyncio import get_event_loop
from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocket


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


@app.post("/predict")  # days you want prediction
async def predict_future_days(request: Predict, current_user: User = Depends(get_current_user)):
    return predict(request=request, current_user=current_user)


@app.post("/register")
def register(request: User):
    return create_user(request=request)


@app.post("/login")
def signin(request: User):
    return login(request=request)


@app.get("/produce")
def kafkaProducerTest():
    broker = ["localhost:9092"]
    topic = "test2"
    pd = MessageProducer(broker, topic)
    msg = {"name": "yewon", "stock": "TEST", "days": 0, "predicted_val": -1}
    res = pd.send_message(msg=msg)
    return res


@app.get("/consume")
def kafkaConsumerTest():
    broker = ["localhost:9092"]
    topic = "test2"
    cs = MessageConsumer(broker, topic)
    cs.receive_message()


def run_consumer():
    broker = ["localhost:9092"]
    topic = "test2"
    consumer = MessageConsumer(broker, topic).consumer
    consumed_list = []
    for msg in consumer:
        data = eval(msg.value)
        data['timestamp'] = msg.timestamp
        consumed_list.append(data)
    return jsonable_encoder(consumed_list)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            consumed = await get_event_loop().run_in_executor(
                None, run_consumer)
            await websocket.send_json(consumed)
    except Exception as e:
        raise Exception(f'Could not process event: {e}')
    finally:
        await websocket.close()
