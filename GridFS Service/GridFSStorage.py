from pymongo import MongoClient
import gridfs

class GridFSStorage:
    def __init__(self, config):
        self.client = MongoClient(config.mongo_uri)
        self.db = self.client[config.db_name]
        self.fs = gridfs.GridFS(self.db)

    def save_file(self, file_content, filename):
        return self.fs.put(file_content, filename=filename)
        