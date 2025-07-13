# utils/directories.py

import os
from utils.messages import log, folder_structure_status

# 📌 Base path utama untuk seluruh project
PROJECT_BASE_PATH = "/content/transcript_project"  # Ganti di sini jika ingin pindah lokasi project

def get_base_path() -> str:
    """
    Mengembalikan path utama dari proyek.
    """
    return PROJECT_BASE_PATH

def get_paths():
    """
    Mengembalikan tuple berisi path: (video, audio, output, logs)
    """
    video_path = os.path.join(PROJECT_BASE_PATH, "video")
    audio_path = os.path.join(PROJECT_BASE_PATH, "audio")
    output_path = os.path.join(PROJECT_BASE_PATH, "output")
    logs_path = os.path.join(PROJECT_BASE_PATH, "logs")
    return video_path, audio_path, output_path, logs_path

def create_project_folders():
    """
    Membuat struktur folder project dan menampilkannya.
    """
    video_path, audio_path, output_path, logs_path = get_paths()

    os.makedirs(video_path, exist_ok=True)
    os.makedirs(audio_path, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(logs_path, exist_ok=True)

    log("Project folders created successfully", icon="📁")
    folder_structure_status(video_path, audio_path, output_path, logs_path)

    return video_path, audio_path, output_path, logs_path
