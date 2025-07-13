import os
from utils.messages import log, show_folder_structure

def create_project_folders(base_path: str):
    video_path = os.path.join(base_path, "video")
    audio_path = os.path.join(base_path, "audio")
    output_path = os.path.join(base_path, "output")
    logs_path = os.path.join(base_path, "logs")

    # Create directories
    os.makedirs(video_path, exist_ok=True)
    os.makedirs(audio_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(logs_path, exist_ok=True)

    log("Project folders created successfully", icon="📁")
    show_folder_structure(video_path, audio_path, output_path, logs_path)

    return video_path, audio_path, output_path, logs_path
