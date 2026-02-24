from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
from GridFSConfig import GridFSConfig
from GridFSStorage import GridFSStorage

app = FastAPI()

config = GridFSConfig()
storage = GridFSStorage(config)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    data = await file.read()
    file_id = storage.save_file(data, file.filename)
    return {"file_id": str(file_id)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)