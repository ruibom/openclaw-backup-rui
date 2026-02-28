from youtube_transcript_api._api import YouTubeTranscriptApi

try:
    # The video ID from the URL https://youtu.be/iTKkoGd3YcM is iTKkoGd3YcM
    transcript_list = YouTubeTranscriptApi().list('iTKkoGd3YcM')
    
    # Check if the list contains any transcripts and try to extract author from there
    if transcript_list:
        # Accessing the first transcript to see its metadata
        first_transcript = next(iter(transcript_list))
        print(f"Video ID: {first_transcript.video_id}")
        # The API documentation or typical usage usually has the 'author' or 'channel_name' attribute
        # However, it might not be directly exposed here.
        # Let's just print the whole object to inspect for channel info.
        print(f"First Transcript Object: {first_transcript}")
        # Let's try to access parent attributes if available
        # If not directly available on 'Transcript' object, it might be in an internal structure
        
    else:
        print("No transcripts found.")

except Exception as e:
    print(f"An error occurred: {e}")
