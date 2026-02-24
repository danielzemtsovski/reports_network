import os

class IngestionConfig:
    def __init__(self):
        self.kafka_bootstrap_servers = os.getenv("KAFKA_URI","kafka:9092")
        self.images_folder = os.getenv("IMAGES_FOLDER",r"messaging_images/tweet_images")
        self.mongo_loader_url = os.getenv("MONGO_LOADER_URL","http://mongo_loader:5000/upload")