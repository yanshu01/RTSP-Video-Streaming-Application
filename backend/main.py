from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2

app = FastAPI()

# RTSP Stream URL (replace with your actual RTSP URL)
RTSP_URL = "rtsp://<username>:<password>@<ip>:<port>/live"

# Video Frame Generator
def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)
    while True:
        success, frame = cap.read()
        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# Endpoint to stream video
@app.get("/video")
async def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")
