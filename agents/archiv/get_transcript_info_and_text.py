from youtube_transcript_api._api import YouTubeTranscriptApi

try:
    ytt_api = YouTubeTranscriptApi()
    transcript_data = ytt_api.fetch(video_id='jIS2eB-rGv0', languages=['en'])
    
    full_transcript = " ".join([snippet.text for snippet in transcript_data])
    
    word_count = len(full_transcript.split())
    
    # Calculate duration
    last_snippet = transcript_data[-1]
    duration_seconds = last_snippet.start + last_snippet.duration
    minutes = int(duration_seconds // 60)
    seconds = int(duration_seconds % 60)
    duration_formatted = f"{minutes:02}:{seconds:02}"
    
    print(f"Word Count: {word_count}")
    print(f"Duration: {duration_formatted}")
    print(f"Transcript: {full_transcript}")
except Exception as e:
    print(f"An error occurred: {e}")
