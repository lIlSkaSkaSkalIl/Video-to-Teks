import os
import subprocess
from utils.messages import log
from utils.directories import get_paths

def embed_subtitle(video_path: str, subtitle_path: str) -> str:
    """
    Embed .srt subtitle into a video file using ffmpeg (softsub MKV).
    
    Args:
        video_path (str): Full path to input video.
        subtitle_path (str): Full path to subtitle (.srt) file.
    
    Returns:
        str: Path to the final video with embedded subtitles.
    """
    # Validate input
    if not os.path.exists(video_path):
        log(f"Video file not found: {video_path}", "❌")
        raise FileNotFoundError()
    if not os.path.exists(subtitle_path):
        log(f"Subtitle file not found: {subtitle_path}", "❌")
        raise FileNotFoundError()

    # Get output directory
    _, _, output_dir, _ = get_paths()
    os.makedirs(output_dir, exist_ok=True)

    # Build output path
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_with_subtitles.mkv")

    # Embed subtitle using ffmpeg
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-i", subtitle_path,
        "-c", "copy",
        "-c:s", "srt",
        "-map", "0",
        "-map", "1",
        output_path
    ]

    log("Embedding subtitles into video (softsub MKV)...", "🎞️")
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check result
    if os.path.exists(output_path):
        size = os.path.getsize(output_path) / (1024 * 1024)
        log(f"Final video saved to: {output_path}", "✅")
        log(f"File size: {size:.2f} MB", "📦")
        return output_path
    else:
        log("Process failed: output file not found.", "❌")
        return ""
