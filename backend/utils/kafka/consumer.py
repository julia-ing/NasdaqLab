from kafka import KafkaConsumer


class MessageConsumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode("utf-8"),
            group_id="my-group",
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            consumer_timeout_ms = 1000
        )

    def receive_message(self):
        try:
            for message in self.consumer:
                print(message)
        except Exception as exc:
            raise exc
