#!/usr/bin/env python3
"""
Sync job applications to Notion database.
Only syncs 4/5 and 5/5 fit scores per job-search-process.md policy.
"""
import os
import re
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
if not NOTION_API_KEY:
    raise ValueError("NOTION_API_KEY not found in environment")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# The Notion database ID (confirmed working)
DATABASE_ID = "3124affb-d00c-81ad-95fe-fc5dc676c3eb"

def parse_application_file(filepath):
    """Parse a markdown application file and extract key fields."""
    content = filepath.read_text()
    
    # Extract company name from heading
    company_match = re.search(r'# (.+?) - ', content)
    company = company_match.group(1) if company_match else filepath.stem
    
    # Extract role
    role = "Unknown Role"
    role_match = re.search(r'\*\*Role\*\*:\s*([^\n]+)', content)
    if role_match:
        role = role_match.group(1).strip()
    else:
        role_match = re.search(r'# .+? - (.+?)\n', content)
        if role_match:
            role = role_match.group(1).strip()
    
    # Extract fit score
    fit_match = re.search(r'Fit Score\*\*:\s*(\d)/5', content)
    fit_score = int(fit_match.group(1)) if fit_match else 0
    
    # Extract job link
    link_match = re.search(r'Job Link\*\*:\s*(https?://\S+)', content)
    job_link = link_match.group(1) if link_match else ""
    
    # Find hiring manager / contact
    contact = ""
    contact_match = re.search(r'\*\*([^\*]+?)\*\*.*?(?:CEO|CRO|VP|Head|Hiring Manager)', content, re.IGNORECASE)
    if contact_match:
        contact = contact_match.group(1).strip()
    
    return {
        "company": company,
        "role": role,
        "fit_score": fit_score,
        "job_link": job_link,
        "contact": contact,
        "filepath": str(filepath),
        "status": "DRAFT"
    }

def create_database_entry(job_data, github_base_url="https://github.com/ruibom/openclaw-backup-rui/blob/main/applications"):
    """Create a new entry in the Notion database."""
    url = "https://api.notion.com/v1/pages"
    
    # Build GitHub link for answers file
    filename = os.path.basename(job_data['filepath'])
    answers_url = f"{github_base_url}/{filename}"
    
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Company": {
                "title": [{"text": {"content": job_data['company']}}]
            },
            "Role": {
                "rich_text": [{"text": {"content": job_data['role']}}]
            },
            "Job Link": {
                "url": job_data['job_link'] if job_data['job_link'] else None
            },
            "Answers File": {
                "url": answers_url
            },
            "Status": {
                "select": {"name": "DRAFT"}
            },
            "Contact Person": {
                "rich_text": [{"text": {"content": job_data['contact']}}]
            },
            "Notes": {
                "rich_text": [{"text": {"content": f"Fit Score: {job_data['fit_score']}/5"}}]
            }
        }
    }
    
    response = requests.post(url, headers=HEADERS, json=payload)
    return response.json()

def list_existing_entries():
    """List existing entries in the database to avoid duplicates."""
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS, json={})
    data = response.json()
    
    existing = []
    for result in data.get("results", []):
        props = result.get("properties", {})
        company_prop = props.get("Company", {}).get("title", [{}])
        if company_prop:
            existing.append(company_prop[0].get("text", {}).get("content", ""))
    return existing

def main():
    apps_dir = Path("/Users/ruibot/.openclaw/workspace/applications")
    
    # Get existing entries to avoid duplicates
    try:
        existing = list_existing_entries()
        print(f"Found {len(existing)} existing entries in Notion")
        for e in existing:
            print(f"  - {e}")
    except Exception as e:
        print(f"Error listing existing entries: {e}")
        existing = []
    
    synced = []
    skipped = []
    
    for md_file in sorted(apps_dir.glob("*.md")):
        job = parse_application_file(md_file)
        
        print(f"\nChecking: {job['company']} - Fit Score: {job['fit_score']}/5")
        
        # Only sync 4/5 and 5/5 fits
        if job["fit_score"] < 4:
            skipped.append(f"{job['company']} ({job['fit_score']}/5 - below threshold)")
            continue
        
        # Check if already exists
        if job["company"] in existing:
            skipped.append(f"{job['company']} (already in Notion)")
            continue
        
        print(f"Syncing: {job['company']} - {job['role']}")
        
        try:
            result = create_database_entry(job)
            if "id" in result:
                page_id = result['id'].replace('-', '')
                synced.append(f"✅ {job['company']} - https://notion.so/{page_id}")
            else:
                error_msg = result.get('message', 'Unknown error')
                synced.append(f"❌ {job['company']} - {error_msg[:80]}")
        except Exception as e:
            synced.append(f"❌ {job['company']} - {e}")
    
    print("\n" + "="*50)
    print("SYNC SUMMARY")
    print("="*50)
    success_count = len([s for s in synced if s.startswith('✅')])
    print(f"\nSynced ({success_count}):")
    for s in synced:
        print(f"  {s}")
    
    print(f"\nSkipped ({len(skipped)}):")
    for s in skipped:
        print(f"  {s}")

if __name__ == "__main__":
    main()
