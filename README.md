# FastAPI And React RTSP Video Streaming Server

This project is a **FastAPI-based RTSP video streaming server** that streams live video from RTSP sources (such as IP cameras) and serves it as an **MJPEG stream** over HTTP.

---

## Features
- **RTSP Support** - Streams live video from RTSP URLs.
- **MJPEG Output** - Serves video frames as MJPEG for browser compatibility.
- **High Performance** - Built using FastAPI for fast and scalable performance.
- **Real-Time Streaming** - Streams frames continuously with low latency.

---

## Tech Stack
- **Backend:** FastAPI, OpenCV, Python
- **Optional Frontend:** React.js 

---

## Installation

### # Clone the Repository
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### # Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### # Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

### # Replace RTSP URL
Update the `RTSP_URL` in `main.py` with your camera's RTSP stream URL:
```python
RTSP_URL = "rtsp://username:password@camera-ip:port/path"
```

### # Start the Server
```bash
uvicorn main:app --reload
```

### # Access the Video Feed
Open the following URL in your browser:
```
http://localhost:8000/video
```

---

## Endpoints
- **`/video`** - Streams video as MJPEG.

---

## Requirements
- **Python 3.8+**
- **RTSP-enabled Camera**

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## Author
[Amod Kumar J](https://github.com/username)

# All right

