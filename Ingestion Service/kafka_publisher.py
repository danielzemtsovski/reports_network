import os
import json
from confluent_kafka import Producer


class KafkaPublisher:
    def __init__(self):
        self.servers = os.getenv("KAFKA_URI", "kafka:9092")
        self.topic = os.getenv("KAFKA_TOPIC", "raw_images")
        
        self.producer = Producer({'bootstrap.servers': self.servers})
        
    def publish_raw(self, event_data):
        self.producer.produce(
            topic=self.topic, 
            value=json.dumps(event_data).encode('utf-8'))
        self.producer.flush()  
        
        
