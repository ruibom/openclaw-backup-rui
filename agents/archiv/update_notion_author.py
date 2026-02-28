import requests
import json

NOTION_TOKEN = '$NOTION_TOKEN'
PAGE_ID = '3154affbd00c8199840fe43a114094e0' # Page ID for 'How to Generate Flawless AI Images'

url = f'https://api.notion.com/v1/pages/{PAGE_ID}'

headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

payload = {
    'properties': {
        'Author': {
            'rich_text': [
                {
                    'text': {
                        'content': 'Jack Roberts'
                    }
                }
            ]
        }
    }
}

try:
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status() # Raise an exception for HTTP errors
    print("Notion page updated successfully!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error updating Notion page: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.json())
