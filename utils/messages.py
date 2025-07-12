# utils/messages.py

def folder_structure_status(video_dir, audio_dir, output_dir, log_dir):
    print("📂 Folder yang dibuat:")
    print(f"   ├─🎞️ Video : {video_dir}")
    print(f"   ├─🎧 Audio : {audio_dir}")
    print(f"   ├─📜 Output: {output_dir}")
    print(f"   └─🧾 Log   : {log_dir}")
