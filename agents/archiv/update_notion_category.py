import requests
import json

NOTION_TOKEN = '$NOTION_TOKEN'
PAGE_ID = '3164affb-d00c-8158-9ec2-d9a125c9968c'

url = f'https://api.notion.com/v1/pages/{PAGE_ID}'

headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

payload = {
    'properties': {
        'Category': {
            'multi_select': [
                {
                    'name': 'Productivity'
                }
            ]
        }
    }
}

try:
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status() # Raise an exception for HTTP errors
    print("Notion page category updated successfully!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error updating Notion page category: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.json())
