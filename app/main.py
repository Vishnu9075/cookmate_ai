import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.transcript.youtube_transcript import fetch_transcript
from modules.parser.parse_transcript import parse_recipe_from_text
from modules.voice.voice_assistant import VoiceAssistant

def main():
    print("📼 CookMate AI - YouTube Transcript Extractor + Parser")
    video_url = input("Paste a YouTube recipe video URL: ").strip()

    try:
        # Step 1: Get transcript
        path = fetch_transcript(video_url)
        print(f"✅ Transcript saved to: {path}")

        # Step 2: Read the transcript text
        with open(path, "r", encoding="utf-8") as f:
            transcript_text = f.read()

        # Step 3: Call OpenAI to parse it
        print("🧠 Parsing transcript with GPT...")
        recipe_json = parse_recipe_from_text(transcript_text)

        # Step 4: Save result to .json
        output_path = path.replace(".txt", "_parsed.json")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(recipe_json)

        print(f"✅ Recipe parsed and saved to: {output_path}")

        assistant = VoiceAssistant(output_path)
        assistant.start_cooking()

    except Exception as e:
        print(f"❌ Error: {e}")

    

if __name__ == "__main__":
    main()
