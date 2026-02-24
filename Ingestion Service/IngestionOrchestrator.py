from fastapi import FastAPI, BackgroundTasks
import uvicorn

import os
from ingestion_config import IngestionConfig
from metadata_extractor import MetadataExtractor
from ocr_engine import OCREngine
from kafka_publisher import KafkaPublisher
from mongo_loader_client import MongoLoaderClient


class IngestionOrchestrator:
    def __init__(self):
        self.config = IngestionConfig()
        self.metadata_extractor = MetadataExtractor()
        self.ocr_engine = OCREngine()
        self.mongo_client = MongoLoaderClient(self.config.mongo_loader_url)
        self.kafka_publisher = KafkaPublisher()

    def run(self):
        folder = self.config.images_folder

        for filename in os.listdir(folder):
            #רק קבצים בסיומת של תמונה
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                # חיבור הנתיב המלא לקובץ הספציפי (בעצם מוסיף את שם הקובץ לנתיב הקיים)
                full_path = os.path.join(folder, filename)
        
                # חילוץ מטאדאטה
                metadata = self.metadata_extractor.process_image(full_path)
                # חילוץ טקסט
                raw_text = self.ocr_engine.process_image(full_path)
                # שליחת קובץ ל-Mongo Loader (FastAPI)
                self.mongo_client.upload_image(full_path)      
                #**-מוסיף לדיקשינרי הזה את המשתנה אחרי הפסיק
                event = {**metadata, "raw_text": raw_text}
                self.kafka_publisher.publish_raw(event)
                        

# ---------------- FASTAPI ----------------

app = FastAPI()

orchestrator = IngestionOrchestrator()

@app.post("/start")
def start(background_tasks: BackgroundTasks):
    #שולח הודעה כבר בהתחלה ולא מחכה שזה יגמר
    background_tasks.add_task(orchestrator.run)
    return {"status": "Ingestion process started in background"}

 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
