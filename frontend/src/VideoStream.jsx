import React from 'react';

const VideoStream = () => {
  return (
    <div>
      <h1>RTSP Stream</h1>
      <img
        src="http://localhost:8000/video" // Replace with your backend URL
        alt="RTSP Stream"
        style={{ width: '50%', height: '50vh' }}
      />
    </div>
  );
};

export default VideoStream;
