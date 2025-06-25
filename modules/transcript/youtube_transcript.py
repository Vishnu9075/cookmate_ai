from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    parsed = urlparse(url)
    if 'youtube.com' in parsed.netloc:
        return parse_qs(parsed.query).get('v', [None])[0]
    elif 'youtu.be' in parsed.netloc:
        return parsed.path[1:]
    return None

def fetch_transcript(video_url):
    """Fetch transcript text from a YouTube video."""
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        raise RuntimeError(f"Failed to get transcript: {e}")

    full_text = "\n".join([entry['text'] for entry in transcript_data])

    output_path = f"data/transcripts/{video_id}.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    return output_path
