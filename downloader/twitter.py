# downloader/twitter.py

import os
import re
import json
import glob
import subprocess
from tqdm import tqdm
from utils.messages import log, show_download_summary

def download_tweet_video(tweet_url: str, video_dir: str, output_dir: str, cookies_path: str = "cookies.txt"):
    # 🆔 Extract Tweet ID
    match = re.search(r"/status/(\d+)", tweet_url)
    if not match:
        raise ValueError("❌ Invalid URL: Tweet ID not found.")
    tweet_id = match.group(1)

    # 🔍 Simulate Metadata
    info = None
    ydl_opts = {
        "quiet": True,
        "simulate": True,
        "extract_flat": True,
        "dump_single_json": True,
    }

    log(f"Fetching tweet metadata... ({tweet_url})", icon="🔍")
    try:
        import yt_dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(tweet_url, download=False)
    except Exception as e:
        log(f"Failed to fetch metadata: {e}", icon="❌")
        if "authentication" in str(e).lower():
            log("Tweet might require cookies.txt (authentication needed).", icon="🔐")

    # 💾 Save metadata
    if info:
        json_path = os.path.join(output_dir, f"tweet_meta_{tweet_id}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        log(f"Metadata saved to: {json_path}", icon="📄")
    else:
        log("Metadata not available or not saved.", icon="⚠️")

    # 🍪 Check for cookies
    use_cookies = os.path.exists(cookies_path)
    log("Using cookies.txt" if use_cookies else "Not using cookies", icon="🔐" if use_cookies else "🔓")

    # 📥 Prepare yt-dlp command
    log("Starting video download...\n", icon="📥")
    command = ["yt-dlp"]
    if use_cookies:
        command += ["--cookies", cookies_path]
    command += [
        "-f", "best",
        "-o", os.path.join(video_dir, "%(id)s_video.%(ext)s"),
        tweet_url
    ]

    # Run subprocess with tqdm progress bar
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
            print(line)
    process.wait()
    progress_bar.n = 100
    progress_bar.refresh()
    progress_bar.close()

    log("Download complete.", icon="✅")

    # 📦 Summary
    downloaded_files = glob.glob(os.path.join(video_dir, "*_video.*"))
    show_download_summary(tweet_url, tweet_id, use_cookies, info, downloaded_files, video_dir)
