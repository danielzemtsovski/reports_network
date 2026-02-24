import easyocr
import warnings

class OCREngine:
    def __init__(self):
        #מוריד מההדפסה את האזהרות
        warnings.filterwarnings("ignore", category=UserWarning)
        # יצירת הReader, בפונקציה נפרדת כי אני רוצה להפעיל רק פעם אחת 
        self.reader = easyocr.Reader(['en'])

    def process_image(self, image_path):
        # הוצאת הטקסט (כי בלי זה יביא לי גם מיקום של כל מילה בתמונה, detail=0 מחזיר רשימת טקסטים נקייה)
        result = self.reader.readtext(image_path, detail=0)
        return " ".join(result) if result else "No text found"