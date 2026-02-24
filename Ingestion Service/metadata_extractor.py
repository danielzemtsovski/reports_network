import os
import uuid
from PIL import Image

class MetadataExtractor:

    @staticmethod
    def process_image(image):
        image_id = str(uuid.uuid4())
        #קבלת הגודל
        file_size = os.path.getsize(image)
        #img-זה אובייקט
        with Image.open(image) as img:
            metadata = {"id_image": image_id,
                        "bytes_size_file": file_size,
                        "width": img.width,  #רוחב
                        "height": img.height,   #אורך
                        "format_file": img.format,
                        "file_path": image}
        return metadata
