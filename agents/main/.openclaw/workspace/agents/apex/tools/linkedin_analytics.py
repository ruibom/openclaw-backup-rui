#!/usr/bin/env python3
"""
LinkedIn Post Analytics Scraper for Apex
Extracts engagement metrics (views, reactions, comments, reposts)
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

class LinkedInAnalytics:
    def __init__(self, data_dir: str = None):
        self.data_dir = Path(data_dir or "~/.openclaw/workspace/agents/apex/data/linkedin").expanduser()
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.cookies_file = self.data_dir / "cookies.json"
        self.analytics_file = self.data_dir / "post_analytics.json"
        
        # Post history for tracking over time
        self.history_file = self.data_dir / "post_history.jsonl"
        
    async def extract_post_analytics(self, post_url: str) -> dict:
        """Extract analytics from a single LinkedIn post URL"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(
                viewport={"width": 1280, "height": 800},
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            )
            
            if self.cookies_file.exists():
                cookies = json.loads(self.cookies_file.read_text())
                await context.add_cookies(cookies)
            
            page = await context.new_page()
            
            try:
                await page.goto(post_url)
                await page.wait_for_load_state("networkidle")
                
                analytics = await self._scrape_post_data(page)
                analytics["post_url"] = post_url
                
                # Save cookies
                cookies = await context.cookies()
                self.cookies_file.write_text(json.dumps(cookies))
                
                # Save analytics
                self._save_analytics(post_url, analytics)
                self._append_history(analytics)
                
                return analytics
                
            finally:
                await browser.close()
    
    async def _scrape_post_data(self, page) -> dict:
        """Scrape engagement metrics from post page"""
        analytics = {
            "scraped_at": datetime.now().isoformat(),
            "views": None,
            "reactions": None,
            "comments": None,
            "reposts": None,
            "engagement_rate": None,
            "post_text": None,
            "post_date": None
        }
        
        try:
            # Views
            views_selector = "span[data-test-id='social-activity__insights-impression-count']"
            if await page.locator(views_selector).count() > 0:
                views_text = await page.locator(views_selector).inner_text()
                analytics["views"] = self._parse_number(views_text)
            
            # Reactions
            reactions_selector = "button[aria-label*='reaction'] .social-details-social-counts__reactions-count"
            if await page.locator(reactions_selector).count() > 0:
                reactions_text = await page.locator(reactions_selector).inner_text()
                analytics["reactions"] = self._parse_number(reactions_text)
            
            # Comments
            comments_selector = "button[aria-label*='comment'] .social-details-social-counts__comments-count"
            if await page.locator(comments_selector).count() > 0:
                comments_text = await page.locator(comments_selector).first.inner_text()
                analytics["comments"] = self._parse_number(comments_text)
            
            # Reposts
            reposts_selector = "button[aria-label*='repost'] .social-details-social-counts__reposts-count"
            if await page.locator(reposts_selector).count() > 0:
                reposts_text = await page.locator(reposts_selector).inner_text()
                analytics["reposts"] = self._parse_number(reposts_text)
            
            # Engagement rate
            if analytics["views"] and analytics["views"] > 0:
                interactions = (analytics["reactions"] or 0) + (analytics["comments"] or 0)
                analytics["engagement_rate"] = round((interactions / analytics["views"]) * 100, 2)
            
            # Post content preview
            text_selector = ".feed-shared-update-v2__description span, .share-update-card__update-text"
            if await page.locator(text_selector).first.count() > 0:
                analytics["post_text"] = await page.locator(text_selector).first.inner_text()
                
        except Exception as e:
            analytics["error"] = str(e)
        
        return analytics
    
    def _parse_number(self, text: str) -> int:
        text = text.strip().replace(",", "").replace("+", "")
        multiplier = 1
        
        if "K" in text.upper():
            multiplier = 1000
            text = text.upper().replace("K", "")
        elif "M" in text.upper():
            multiplier = 1000000
            text = text.upper().replace("M", "")
        
        try:
            parsed = float(text) * multiplier
            return int(parsed)
        except:
            return 0
    
    def _save_analytics(self, post_url: str, analytics: dict):
        post_id = post_url.split("?")[0].split("/")[-1] or post_url
        all_analytics = json.loads(self.analytics_file.read_text()) if self.analytics_file.exists() else {}
        all_analytics[post_id] = analytics
        self.analytics_file.write_text(json.dumps(all_analytics, indent=2))
    
    def _append_history(self, analytics: dict):
        """Append to history for time-series analysis"""
        with open(self.history_file, "a") as f:
            f.write(json.dumps(analytics) + "\n")
    
    def get_analytics(self, post_url: str = None) -> dict:
        if not self.analytics_file.exists():
            return {}
        
        all_analytics = json.loads(self.analytics_file.read_text())
        
        if post_url:
            post_id = post_url.split("?")[0].split("/")[-1] or post_url
            return all_analytics.get(post_id, {})
        
        return all_analytics

async def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: linkedin_analytics.py <post_url>")
        print("Or: linkedin_analytics.py --get <post_url>")
        sys.exit(1)
    
    tool = LinkedInAnalytics()
    
    if sys.argv[1] == "--get":
        post_url = sys.argv[2] if len(sys.argv) > 2 else None
        analytics = tool.get_analytics(post_url)
        print(json.dumps(analytics, indent=2))
    else:
        post_url = sys.argv[1]
        analytics = await tool.extract_post_analytics(post_url)
        print(json.dumps(analytics, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
