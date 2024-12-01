import os
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import io
import uvicorn
import numpy as np
import nest_asyncio
from enum import Enum
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

dir_name = "images_uploaded"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

app = FastAPI(title='Deploying a ML Model with FastAPI')

@app.get("/")
def home():
    return "Working fine ..."

@app.post("/predict") 
def prediction(file: UploadFile = File(...)):

    filename = file.filename
    fileExtension = filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not fileExtension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")
        
    image_stream = io.BytesIO(file.file.read())
    image_stream.seek(0)
    file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    bbox, label, conf = cv.detect_common_objects(image, model='yolov3-tiny')
    output_image = draw_bbox(image, bbox, label, conf)
    cv2.imwrite(f'{dir_name}/{filename}', output_image)
    file_image = open(f'{dir_name}/{filename}', mode="rb")
    return StreamingResponse(file_image, media_type="image/jpeg")
