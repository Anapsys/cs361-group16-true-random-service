import yt_dlp
import cv2
import numpy as np
from fastapi import FastAPI, HTTPException

app = FastAPI()

URL = "https://www.youtube.com/watch?v=1rvCfsW_qTA"


def get_ran_px():

    # extracts livestream URL and metadata without downloading
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(URL, download=False)
        stream_url = info['url']

        if not info.get('is_live', False):
            raise HTTPException(status_code=400, detail="Livestream currently offline")

    capture_video = cv2.VideoCapture(stream_url)

    # ret = True, False (status of the capture)
    # frame = store the 3D array
    ret, frame = capture_video.read()
    capture_video.release()

    if ret:

        # prints the whole array (BGR values)
        # print("Full Frame: ")
        # print(frame)

        # dimensions of the frame:
        # (Height, Width, num of BGR values per row)
        # print("Frame Dimensions: ")
        # print(frame.shape)
        pass

    if not ret:
        raise HTTPException(status_code=404, detail="Livestream data not found")

    # height, width, px BGR value indices
    h, w, px = frame.shape

    # get random pixel
    h_px = np.random.randint(0, h)
    w_px = np.random.randint(0, w)
    c_px = np.random.randint(0, px)

    # random pixel from a single still frame of the livestream
    pixel_value = int(frame[h_px, w_px, c_px])

    # print("Random Pixel Indices", h_px, w_px, c_px)
    # print("Random Pixel [BGR Values]", frame[h_px, w_px])
    print(pixel_value)
    return pixel_value


get_ran_px()
