import os
import requests

class MongoLoaderClient:
    def __init__(self, upload_url):
        self.upload_url = upload_url
        
    def upload_image(self, image_path):
        try:
            #rb = read binary כי ביקשו לשלוח בבינארי
            with open(image_path, "rb") as f:
                #path.basename(image_path)-שם הקובץ בלי הסיומת
                files = {"file": (os.path.basename(image_path), f)}
                response = requests.post(self.upload_url, files=files)
            return response.status_code == 200
        except Exception:
            return False