import os
import subprocess
from utils.messages import log
from utils.directories import get_paths

def extract_subtitle_from_video(video_path: str) -> str:
    """
    Extract the first soft subtitle track from a video file and save as .srt
    
    Args:
        video_path (str): Full path to input video
    
    Returns:
        str: Path to the extracted .srt file, or empty string if none found
    """
    if not os.path.exists(video_path):
        log(f"Video file not found: {video_path}", "❌")
        raise FileNotFoundError()

    _, _, output_dir, _ = get_paths()
    os.makedirs(output_dir, exist_ok=True)

    # Detect subtitle stream
    log("Checking for subtitle stream in video...", "🔍")
    cmd_check = [
        "ffprobe", "-loglevel", "error",
        "-select_streams", "s",
        "-show_entries", "stream=index:stream_tags=language",
        "-of", "default=noprint_wrappers=1",
        video_path
    ]
    result = subprocess.run(cmd_check, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subtitle_info = result.stdout.strip()

    if not subtitle_info:
        log("No subtitle stream found in the video.", "⚠️")
        return ""

    # Extract subtitle
    log("Subtitle found! Extracting to .srt...", "📤")
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    srt_output_path = os.path.join(output_dir, f"{base_name}_extracted.srt")

    cmd_extract = [
        "ffmpeg", "-y", "-i", video_path,
        "-map", "0:s:0",
        srt_output_path
    ]
    subprocess.run(cmd_extract, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if os.path.exists(srt_output_path):
        size_kb = os.path.getsize(srt_output_path) / 1024
        log(f"Subtitle extracted successfully: {srt_output_path}", "✅")
        log(f"File size: {size_kb:.2f} KB", "📦")
        return srt_output_path
    else:
        log("Extraction failed: .srt file not found.", "❌")
        return ""
