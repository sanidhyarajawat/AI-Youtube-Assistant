from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, JSONFormatter

def get_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi().fetch(video_id)
    # formatter = TextFormatter()
    formatter = JSONFormatter()
    print("transcript", transcript)
    return formatter.format_transcript(transcript)

def extract_video_id(url: str) -> str:
    # Supports various formats
    import re
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    return match.group(1) if match else None