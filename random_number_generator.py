import yt_dlp
import cv2
import numpy as np


# -----------------YouTube livestream URLs------------------ #
# Uses the Jellyfish Tank URL first; others are backups

URLs = [
    # Jellyfish Tank
    "https://www.youtube.com/watch?v=1rvCfsW_qTA",

    # Tropical Reef Aquarium
    "https://www.youtube.com/watch?v=DHUnz4dyb54",

    # Polar Bear Tundra
    "https://www.youtube.com/watch?v=kvJnsuyE0cs"
]


# yt-dlp set options
options = {
    "quiet": True,
    "no_warnings": True,
    "logger": None
}


def get_valid_stream():
    for url in URLs:
        # Extracts livestream URL and metadata without downloading
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=False)
            if info.get('is_live', False):
                return info['url']
                break
    else:
        print("Livestreams are offline")
        return
    

def get_single_frame():
    # Capture Frame
    stream_url = get_valid_stream()
    capture_video = cv2.VideoCapture(stream_url)
    ret, frame = capture_video.read()
    capture_video.release()

    if not ret:
        print("Capture Frame Failed")
        return -1
    else:
        return frame


def get_rand_px():
    """
    Capture a single frame from a livestream and
    return a random pixel's RGB value

    Returns:
        int: Random pixel RGB value
        None: if the capture failed
    """

    frame = get_single_frame()
    # Get a random pixel's RGB value
    h, w, px = frame.shape
    pixel_value = int(frame[np.random.randint(0, h), np.random.randint(0, w),
                            np.random.randint(0, px)])
    print(pixel_value)
    return pixel_value


if __name__ == "__main__":
    get_rand_px()
