# Notion Integration

## API Key
NOTION_API_KEY=$NOTION_TOKEN

## Job Tracker Database
DATABASE_ID=3134affb-d00c-81e7-8d5a-ecb12aac8f98
URL=https://www.notion.so/3134affbd00c81e78d5aecb12aac8f98

## Usage
When making Notion API calls, always use:
- Authorization: Bearer $NOTION_TOKEN
- Notion-Version: 2022-06-28
- Database ID: 3134affb-d00c-81e7-8d5a-ecb12aac8f98

## Test (run to verify access)
curl -s https://api.notion.com/v1/databases/3134affb-d00c-81e7-8d5a-ecb12aac8f98 \
  -H "Authorization: Bearer $NOTION_TOKEN" \
  -H "Notion-Version: 2022-06-28"
