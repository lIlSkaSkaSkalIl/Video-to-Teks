import os
import json
import textwrap
from datetime import timedelta
from utils.messages import log
from utils.directories import get_paths

def seconds_to_srt_time(seconds: float) -> str:
    t = timedelta(seconds=seconds)
    full = str(t).split(".")[0].zfill(8)
    ms = f"{int(t.microseconds / 1000):03d}"
    return f"{full},{ms}"

def wrap_text(text: str, width: int = 80) -> str:
    return "\n".join(textwrap.wrap(text, width=width))

def export_to_srt(json_path: str, max_chars_per_line: int = 80) -> str:
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"❌ File not found: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        segments = json.load(f)

    log(f"Reading transcript from: {json_path}", "📄")
    log(f"Number of segments: {len(segments)}", "🔢")

    srt_lines = []
    for idx, seg in enumerate(segments, 1):
        start = seconds_to_srt_time(seg["start"])
        end = seconds_to_srt_time(seg["end"])
        text = wrap_text(seg["text"].strip(), width=max_chars_per_line)

        srt_lines.append(f"{idx}")
        srt_lines.append(f"{start} --> {end}")
        srt_lines.append(text)
        srt_lines.append("")

    # Save output to the same base name as JSON
    _, _, output_dir, _ = get_paths()
    json_base = os.path.splitext(os.path.basename(json_path))[0]
    srt_path = os.path.join(output_dir, f"{json_base}.srt")

    with open(srt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    log("Subtitle successfully saved to:", "✅")
    print(f"📍 {srt_path}")
    return srt_path
