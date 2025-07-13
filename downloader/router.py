# downloader/router.py

import os
from datetime import datetime
from utils.messages import log, show_download_info

def prepare_download(video_url: str, download_type: str, file_name: str, video_dir: str) -> str:
    """
    Prepare the final output path and valid filename for video download.

    Returns the full output_path.
    """
    os.makedirs(video_dir, exist_ok=True)
    log("Video folder is ready.", icon="📂")

    # Generate filename if not provided
    if not file_name.strip():
        timestamp = datetime.now().strftime("video_%Y%m%d_%H%M%S")
        file_name = f"{timestamp}.mp4"
        log("Filename generated based on current time.", icon="🕒")
    elif not file_name.endswith(".mp4"):
        file_name += ".mp4"
        log("Added .mp4 extension to the filename.", icon="✏️")

    output_path = os.path.join(video_dir, file_name)
    show_download_info(video_url, download_type, output_path)

    return output_path
