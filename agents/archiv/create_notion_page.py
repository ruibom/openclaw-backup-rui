import requests
import json

NOTION_TOKEN = '$NOTION_TOKEN'
NOTION_DATABASE_ID = '3144affb-d00c-813f-a989-e0d4c1341c35'

video_title = "Game Theory #9: The US-Iran War"
video_url = "https://youtu.be/jIS2eB-rGv0?si=9oqgMB5HV9nGZgbV"
video_type = "YouTube"
video_category = ["AI"] # User instruction: save under AI
video_summary = "This video, presented by Professor Jiang, analyzes a hypothetical US-Iran conflict through the lens of game theory. It outlines the strategic objectives and vulnerabilities of both sides, including alleged Iranian actions like attacks on the GCC and potential closure of the Strait of Hormuz, which could collapse the petro-dollar system and impact global economies. The discussion highlights the asymmetry in warfare, Iran's religious motivations for martyrdom and jihad, and the US/Israeli strategy to exploit Iran's water and ethnic divisions. It also explores the broader geopolitical implications, including potential involvement from global powers and the vulnerability of the GCC due to its reliance on food imports and American protection."
video_key_takeaways = [
    "• Conflict Dynamics: The US-Iran conflict is framed as an asymmetric war, driven by Iranian religious motivations (martyrdom, jihad) and US/Israeli geopolitical strategies, with potential for global escalation.",
    "• Strait of Hormuz Significance: Its potential closure by Iran poses an existential threat to global oil supplies and the petro-dollar, severely impacting economies like Japan, China, and India.",
    "• GCC Vulnerability: Gulf Cooperation Council countries are presented as economically fragile, dependent on US protection and food/water imports, making them strategic targets for Iran.",
    "• Asymmetric Warfare: Iran's use of cheap, numerous drones against expensive US defense systems highlights a fundamental mismatch in military strategy and cost-effectiveness.",
    "• Water and Ethnicity as Weapons: Both sides are depicted as exploiting water scarcity and ethnic divisions as strategic weaknesses against their adversaries, leading to potential internal strife and refugee crises."
]
video_author = "Professor Jiang"
video_source = "YouTube"
video_rating = "⭐⭐⭐⭐ Great"
video_related_to = "geopolitics, US-Iran conflict, game theory, Middle East, economic impact, military strategy, petrodollar" # User instruction: add to geopolitics tagging
video_language = "English"
video_word_count = 6256
video_duration = "44:39"

payload = {
    "parent": { "database_id": NOTION_DATABASE_ID },
    "properties": {
      "Title": {
        "title": [
          {
            "text": {
              "content": video_title
            }
          }
        ]
      },
      "Source URL": {
        "url": video_url
      },
      "Type": {
        "select": {
          "name": video_type
        }
      },
      "Category": {
        "multi_select": [{"name": cat} for cat in video_category]
      },
      "Summary": {
        "rich_text": [
          {
            "text": {
              "content": video_summary
            }
          }
        ]
      },
      "Key Takeaways": {
        "rich_text": [
          {"text": {"content": takeaway}} for takeaway in video_key_takeaways
        ]
      },
      "Author": {
        "rich_text": [
          {
            "text": {
              "content": video_author
            }
          }
        ]
      },
      "Source": {
        "select": {
          "name": video_source
        }
      },
      "Rating": {
        "select": {
          "name": video_rating
        }
      },
      "Related To": {
        "rich_text": [
          {
            "text": {
                "content": video_related_to
            }
          }
        ]
      },
      "Saved Date": {
        "date": {
          "start": "2026-03-03"
        }
      },
      "Read": {
        "checkbox": False
      },
      "Favorite": {
        "checkbox": False
      },
      "Language": {
        "select": {
          "name": video_language
        }
      },
      "Word Count": {
        "number": video_word_count
      },
      "Duration": {
        "rich_text": [
          {
            "text": {
              "content": video_duration
            }
          }
        ]
      }
    }
}

try:
    response = requests.post('https://api.notion.com/v1/pages', headers={
        'Authorization': f'Bearer {NOTION_TOKEN}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    response.raise_for_status()
    print("Notion page created successfully!")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error creating Notion page: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(e.response.text)
