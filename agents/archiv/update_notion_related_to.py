import requests
import json

NOTION_TOKEN = '$NOTION_TOKEN'
PAGE_ID = '3174affb-d00c-81f5-80f2-f9d8bc9db704'

url = f'https://api.notion.com/v1/pages/{PAGE_ID}'

headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

payload = {
    'properties': {
        'Related To': {
            'rich_text': [
                {
                    'text': {
                        'content': 'life, wisdom, government, surveillance, privacy, conspiracy, intelligence agencies'
                    }
                }
            ]
        }
    }
}

try:
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status() # Raise an exception for HTTP errors
    print("Notion page 'Related To' updated successfully!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error updating Notion page 'Related To': {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.json())
