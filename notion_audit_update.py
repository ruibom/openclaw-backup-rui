#!/usr/bin/env python3
"""
Update Notion database entries per audit requirements:
1. Eftsure - Fix fit score from 0/5 → 4/5 in Notes field
2. Webflow - Mark as CLOSED/REJECTED (job removed)
3. CrowdStrike - Mark as CLOSED/REJECTED (job removed)
4. Madison Logic - Archive/Delete (3/5 fit - below threshold)
5. Vatica Health - Archive/Delete (2/5 fit - below threshold)
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}
DATABASE_ID = "3124affb-d00c-81ad-95fe-fc5dc676c3eb"

def query_database():
    """Query all entries in the database."""
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS, json={})
    return response.json()

def update_page(page_id, properties):
    """Update a Notion page with new properties."""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {"properties": properties}
    response = requests.patch(url, headers=HEADERS, json=payload)
    return response.json()

def archive_page(page_id):
    """Archive a Notion page (soft delete)."""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {"archived": True}
    response = requests.patch(url, headers=HEADERS, json=payload)
    return response.json()

def main():
    print("Fetching Notion database entries...")
    data = query_database()
    
    if "results" not in data:
        print(f"Error: {data}")
        return
    
    # Map company names to page IDs
    company_map = {}
    for result in data["results"]:
        props = result.get("properties", {})
        company_prop = props.get("Company", {}).get("title", [{}])
        if company_prop:
            company_name = company_prop[0].get("text", {}).get("content", "")
            company_map[company_name] = {
                "page_id": result["id"],
                "properties": props
            }
    
    print(f"\nFound {len(company_map)} entries in database")
    for name in company_map:
        print(f"  - {name}")
    
    updates = []
    
    # 1. Update Eftsure - Fix fit score to 4/5
    if "Eftsure" in company_map:
        page_id = company_map["Eftsure"]["page_id"]
        print(f"\n📝 Updating Eftsure: Setting fit score to 4/5...")
        result = update_page(page_id, {
            "Notes": {
                "rich_text": [{"text": {"content": "Fit Score: 4/5"}}]
            }
        })
        if "id" in result:
            updates.append("✅ Eftsure: Updated fit score to 4/5")
        else:
            updates.append(f"❌ Eftsure: {result.get('message', 'Error')}")
    
    # 2. Mark Webflow as CLOSED/REJECTED
    if "Webflow" in company_map:
        page_id = company_map["Webflow"]["page_id"]
        print(f"\n📝 Updating Webflow: Marking as REJECTED (job removed)...")
        result = update_page(page_id, {
            "Status": {"select": {"name": "REJECTED"}},
            "Notes": {
                "rich_text": [{"text": {"content": "Job removed - 404 error. Closed position."}}]
            }
        })
        if "id" in result:
            updates.append("✅ Webflow: Status → REJECTED (job removed)")
        else:
            updates.append(f"❌ Webflow: {result.get('message', 'Error')}")
    
    # 3. Mark CrowdStrike as CLOSED/REJECTED
    if "CrowdStrike" in company_map:
        page_id = company_map["CrowdStrike"]["page_id"]
        print(f"\n📝 Updating CrowdStrike: Marking as REJECTED (job filled)...")
        result = update_page(page_id, {
            "Status": {"select": {"name": "REJECTED"}},
            "Notes": {
                "rich_text": [{"text": {"content": "Job filled/removed - 404 error. Closed position."}}]
            }
        })
        if "id" in result:
            updates.append("✅ CrowdStrike: Status → REJECTED (job filled)")
        else:
            updates.append(f"❌ CrowdStrike: {result.get('message', 'Error')}")
    
    # 4. Archive Madison Logic (3/5 fit - below threshold)
    if "Madison Logic" in company_map:
        page_id = company_map["Madison Logic"]["page_id"]
        print(f"\n🗑️ Archiving Madison Logic: 3/5 fit (below threshold)...")
        result = archive_page(page_id)
        if "id" in result:
            updates.append("✅ Madison Logic: Archived (3/5 fit - below threshold)")
        else:
            updates.append(f"❌ Madison Logic: {result.get('message', 'Error')}")
    
    # 5. Archive Vatica Health (2/5 fit - below threshold)
    if "Vatica Health" in company_map:
        page_id = company_map["Vatica Health"]["page_id"]
        print(f"\n🗑️ Archiving Vatica Health: 2/5 fit (below threshold)...")
        result = archive_page(page_id)
        if "id" in result:
            updates.append("✅ Vatica Health: Archived (2/5 fit - below threshold)")
        else:
            updates.append(f"❌ Vatica Health: {result.get('message', 'Error')}")
    
    print("\n" + "="*60)
    print("NOTION UPDATE SUMMARY")
    print("="*60)
    for update in updates:
        print(f"  {update}")
    print("\n✨ All audit updates completed!")

if __name__ == "__main__":
    main()
