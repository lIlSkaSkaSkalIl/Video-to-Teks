# utils/messages.py
# ┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼
import os

def log(msg, icon="📌"):
    print(f"{icon} {msg}")
    
def folder_structure_status(video_dir, audio_dir, output_dir, log_dir):
    print("📂 Folder yang dibuat:")
    print(f"   ┌─🎞️ Video : {video_dir}")
    print(f"   ├─🎧 Audio : {audio_dir}")
    print(f"   ├─📜 Output: {output_dir}")
    print(f"   └─🧾 Log   : {log_dir}")

def show_download_summary(tweet_url, tweet_id, use_cookies, elapsed, downloaded_files, video_dir):
    print("\n📊 Download Summary:")
    print(f"┌─📌 Tweet URL        : {tweet_url}")
    print(f"├─🆔 Tweet ID         : {tweet_id}")
    print(f"├─🔐 Cookies Used     : {'✅ Yes' if use_cookies else '❌ No'}")
    print(f"├─💾 Elapsed Time     : {elapsed:.2f} sec")
    print(f"├─📁 Videos Downloaded: {len(downloaded_files)} file(s)")
    print(f"├─📂 Saved To         : {video_dir}")
    print(f"└─📜 File List        :")

    for i, f in enumerate(downloaded_files, 1):
        fname = os.path.basename(f)
        print(f"   {i}. {fname}")
        info_path = f"{os.path.splitext(f)[0]}.info.json"
        if os.path.exists(info_path):
            try:
                with open(info_path, "r", encoding="utf-8") as meta_file:
                    meta = json.load(meta_file)
                width = meta.get("width") or "?"
                height = meta.get("height") or "?"
                resolution = f"{width}x{height}" if width and height else "?"
                size_mb = os.path.getsize(f) / (1024 * 1024)
                duration = meta.get("duration") or "?"
                print(f"      └─🎞️ Resolution : {resolution}")
                print(f"      └─💾 File Size  : {size_mb:.2f} MB")
                print(f"      └─⏱️ Duration   : {duration} sec")
            except Exception as e:
                print(f"      └─⚠️ Failed to read metadata: {e}")
        else:
            print(f"      └─⚠️ Metadata not found.")

def show_download_info(video_url, download_type, output_path):
    print(f"┌─🎯 Link: {video_url}")
    print(f"├─🧩 Jenis Unduhan: {download_type}")
    print(f"└─📁 File akan disimpan di: {output_path}")

def download_summary(path):
    if os.path.exists(path):
        size = os.path.getsize(path) / (1024 * 1024)
        print(f"\n✅ Selesai! File disimpan di: {path}")
        print(f"📦 Ukuran file: {size:.2f} MB")
    else:
        log("Download selesai tapi file tidak ditemukan.", icon="⚠️")

def show_tool_detection(tool):
    log(f"Menggunakan alat unduhan: {tool}", icon="🚀")

def audio_success(path, size_str):
    print(f"┌─📍 Lokasi Output : {path}")
    print(f"└─📦 Ukuran Audio  : {size_str}")
