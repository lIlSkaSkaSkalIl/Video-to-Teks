# utils/cookies_uploader.py

import os
from utils.messages import log

def process_uploaded_cookies(file_dict: dict, target_name="cookies.txt") -> str | None:
    """
    Rename and validate uploaded cookies file.
    Returns the final cookies file path if valid, otherwise None.
    """
    cookies_file = None

    # Find .txt file
    for filename in file_dict.keys():
        if filename.endswith(".txt"):
            cookies_file = filename
            break

    if cookies_file and os.path.exists(cookies_file):
        if cookies_file != target_name:
            os.rename(cookies_file, target_name)
            log(f"Renamed '{cookies_file}' to '{target_name}'", icon="✏️")
        else:
            log("Cookies file is already named 'cookies.txt'", icon="✅")

        # Preview content
        print("📄 Preview of cookies.txt:")
        with open(target_name, "r", encoding="utf-8") as f:
            for _ in range(3):
                line = f.readline()
                if line:
                    print("   ", line.strip())

        return target_name
    else:
        log("❌ No valid .txt cookies file found or upload failed.", icon="⚠️")
        return None
