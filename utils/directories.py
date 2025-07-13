# utils/directories.py

import os
from utils.messages import log, folder_structure_status

def create_project_folders(base_path: str):
    """
    Create folder structure for video, audio, output, and logs inside base_path.
    """
    video_dir = os.path.join(base_path, "video")
    audio_dir = os.path.join(base_path, "audio")
    output_dir = os.path.join(base_path, "output")
    log_dir = os.path.join(base_path, "logs")

    # Create all folders
    for path in (video_dir, audio_dir, output_dir, log_dir):
        os.makedirs(path, exist_ok=True)

    log("Project folders created successfully", icon="📁")
    folder_structure_status(video_dir, audio_dir, output_dir, log_dir)

    return video_dir, audio_dir, output_dir, log_dir
