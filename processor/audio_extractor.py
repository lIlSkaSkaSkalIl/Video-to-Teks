# processor/audio_extractor.py

import os
import subprocess
from utils.messages import log, audio_success

def human_readable_size(size_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def extract_audio_from_video(video_input_path: str, audio_output_dir: str) -> str:
    os.makedirs(audio_output_dir, exist_ok=True)

    # 🎬 Generate audio path
    video_name = os.path.splitext(os.path.basename(video_input_path))[0]
    audio_path = os.path.join(audio_output_dir, f"{video_name}.wav")

    # ♻️ Hapus jika file sudah ada
    if os.path.exists(audio_path):
        os.remove(audio_path)
        log("Existing audio file found and deleted", icon="♻️")

    # 🔊 Ekstraksi menggunakan ffmpeg
    log("Extracting audio from video...", icon="🔊")
    print(f"🎬 Input Video  : {video_input_path}")
    print(f"🎧 Output Audio : {audio_path}")

    command = [
        "ffmpeg",
        "-i", video_input_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        audio_path,
        "-y",
        "-loglevel", "error"
    ]
    subprocess.run(command)

    # ✅ Konfirmasi
    if os.path.exists(audio_path):
        size_str = human_readable_size(os.path.getsize(audio_path))
        log("Audio extracted successfully!", icon="✅")
        audio_success(audio_path, size_str)
    else:
        log("Audio extraction failed.", icon="❌")

    return audio_path
