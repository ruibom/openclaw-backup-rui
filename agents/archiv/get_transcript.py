from youtube_transcript_api._api import YouTubeTranscriptApi

try:
    ytt_api = YouTubeTranscriptApi()
    transcript_data = ytt_api.fetch(video_id='jIS2eB-rGv0', languages=['en'])
    
    full_transcript = " ".join([snippet.text for snippet in transcript_data])
    
    print(full_transcript)
except Exception as e:
    print(f"An error occurred: {e}")
