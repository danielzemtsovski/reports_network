import os

class GridFSConfig:
    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
        self.db_name = os.getenv("MONGO_DB", "image_storage")