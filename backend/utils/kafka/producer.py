from kafka import KafkaProducer 
import json


class MessageProducer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.broker,
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
            acks=0,
            compression_type='gzip',
        )

    def send_message(self, msg, auto_close=True):
        try:
            future = self.producer.send(self.topic, value=msg)
            self.producer.flush()
            if auto_close:
                self.producer.close()
            future.get()
            return {"status_code": 200}
        except Exception as exc:
            raise exc
