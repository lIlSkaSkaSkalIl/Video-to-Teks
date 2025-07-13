import os
import time
import json
import whisper
from utils.messages import log
from utils.directories import get_paths

def transcribe_audio(audio_path: str, model_name: str = "base") -> str:
    """
    Transcribe audio using OpenAI Whisper and save the segments as JSON.
    
    Args:
        audio_path (str): Path to input audio file (.wav, etc).
        model_name (str): Whisper model to use ("tiny", "base", "small", "medium", "large").
    
    Returns:
        str: Path to saved JSON segments.
    """
    # Validate input file
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"❌ File not found: {audio_path}")
    
    # Get output directory from project structure
    _, _, output_dir, _ = get_paths()
    os.makedirs(output_dir, exist_ok=True)

    # Load model and run transcription
    log(f"Loading Whisper model: {model_name}", "🧠")
    start_time = time.time()

    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, verbose=True)

    end_time = time.time()
    log(f"Transcription completed in {end_time - start_time:.2f} seconds", "⏱️")

    # Save segments to JSON
    json_output_path = os.path.join(output_dir, "segments.json")
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(result["segments"], f, ensure_ascii=False, indent=2)

    # Show preview
    log(f"Transcription saved to: {json_output_path}", "✅")
    log("Text preview:", "📝")
    print(result["text"][:100] + "...")

    return json_output_path
