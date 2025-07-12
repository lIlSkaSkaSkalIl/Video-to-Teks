# utils/messages.py
# ┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼
def log(msg, icon="📌"):
    print(f"{icon} {msg}")
    
def folder_structure_status(video_dir, audio_dir, output_dir, log_dir):
    print("📂 Folder yang dibuat:")
    print(f"   ├─🎞️ Video : {video_dir}")
    print(f"   ├─🎧 Audio : {audio_dir}")
    print(f"   ├─📜 Output: {output_dir}")
    print(f"   └─🧾 Log   : {log_dir}")

def show_download_summary(tweet_url, tweet_id, use_cookies, info, downloaded, video_dir):
    import os, datetime
    file_names = [os.path.basename(f) for f in downloaded]
    total_size_mb = sum(os.path.getsize(f) for f in downloaded) / (1024 * 1024)

    print("\n📊 Ringkasan Status:")
    print(f"┌─📌 URL Tweet       : {tweet_url}")
    print(f"├─🆔 ID Tweet        : {tweet_id}")
    print(f"├─🔐 Cookies         : {'✅ Digunakan' if use_cookies else '❌ Tidak digunakan'}")
    print(f"├─📄 Metadata JSON   : {'✅ Tersimpan' if info else '❌ Tidak ada'}")
    print(f"├─📁 Total Video     : {len(downloaded)} file")
    print(f"├─💾 Ukuran Total    : {total_size_mb:.2f} MB")
    print(f"├─🕒 Selesai pada    : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"├─📂 Lokasi Video    : {video_dir}")
    print(f"└─📜 Daftar File     :")
    for i, fname in enumerate(file_names, 1):
        print(f"     {i}. {fname}")

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
