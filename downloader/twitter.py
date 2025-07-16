import os
import re
import json
import glob
import subprocess
import time
from tqdm import tqdm
from utils.messages import log, show_download_summary

def download_tweet_video(tweet_url: str, video_dir: str, output_dir: str, cookies_path: str = "cookies.txt"):
    # 🆔 Extract Tweet ID
    match = re.search(r"/status/(\d+)", tweet_url)
    if not match:
        raise ValueError("❌ Invalid URL: Tweet ID not found.")
    tweet_id = match.group(1)

    # 📁 Buat direktori jika belum ada
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # 🍪 Cek cookies
    use_cookies = os.path.exists(cookies_path)
    cookie_args = ["--cookies", cookies_path] if use_cookies else []

    # 📥 Mulai download
    log("Starting tweet video download...", "📥")
    start_time = time.time()

    output_template = os.path.join(video_dir, "%(id)s.%(ext)s")
    command = [
        "yt-dlp",
        "-f", "best",
        "--write-info-json",
        "-o", output_template,
    ] + cookie_args + [tweet_url]

    progress_bar = tqdm(total=100, desc="📥 Download", unit="%")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in process.stdout:
        line = line.strip()
        if "%" in line:
            match = re.search(r'(\d{1,3}\.\d)%', line)
            if match:
                percent = float(match.group(1))
                progress_bar.n = int(percent)
                progress_bar.refresh()
        elif "[download]" in line or "Destination" in line:
            log(line)
    process.wait()
    progress_bar.n = 100
    progress_bar.refresh()
    progress_bar.close()

    end_time = time.time()
    elapsed = round(end_time - start_time, 2)
    log("Download completed.", "✅")

    # 📦 Kumpulkan video yang berhasil diunduh
    video_exts = (".mp4", ".mkv", ".webm", ".mov", ".avi")
    downloaded_files = [
        os.path.join(video_dir, f)
        for f in os.listdir(video_dir)
        if f.lower().endswith(video_exts)
    ]

    # 📄 Baca metadata dari .info.json
    for video_file in downloaded_files:
        info_file = f"{os.path.splitext(video_file)[0]}.info.json"
        if os.path.exists(info_file):
            try:
                with open(info_file, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                # Simpan metadata ke output_dir
                meta_save_path = os.path.join(output_dir, f"tweet_meta_{tweet_id}.json")
                with open(meta_save_path, "w", encoding="utf-8") as out:
                    json.dump(meta, out, ensure_ascii=False, indent=2)
                log(f"Metadata saved to: {meta_save_path}", icon="📄")
            except Exception as e:
                log(f"Failed to read/save metadata: {e}", icon="⚠️")
        else:
            log("Metadata not found (.info.json missing)", icon="⚠️")

show_download_summary(
    tweet_url=tweet_url,
    tweet_id=tweet_id,
    use_cookies=use_cookies,
    elapsed=elapsed,
    downloaded_files=downloaded_files,
    video_dir=video_dir
)
