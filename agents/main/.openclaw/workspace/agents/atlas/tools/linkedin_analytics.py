#!/usr/bin/env python3
"""
LinkedIn Post Analytics Scraper for Atlas
Extracts engagement metrics without browser extension requirements
"""

import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright, Page, Browser, BrowserContext

class LinkedInAnalytics:
    def __init__(self, data_dir: str = None):
        self.data_dir = Path(data_dir or "~/.openclaw/workspace/agents/atlas/data/linkedin").expanduser()
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.cookies_file = self.data_dir / "cookies.json"
        self.analytics_file = self.data_dir / "post_analytics.json"
        
    async def extract_post_analytics(self, post_url: str) -> dict:
        """Extract analytics from a single LinkedIn post URL"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)  # Headless detection risk
            context = await browser.new_context(
                viewport={"width": 1280, "height": 800},
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            )
            
            # Load existing cookies if available
            if self.cookies_file.exists():
                cookies = json.loads(self.cookies_file.read_text())
                await context.add_cookies(cookies)
            
            page = await context.new_page()
            
            try:
                # Navigate to post
                await page.goto(post_url)
                await page.wait_for_load_state("networkidle")
                
                # Extract analytics
                analytics = await self._scrape_post_data(page)
                
                # Save cookies for next time
                cookies = await context.cookies()
                self.cookies_file.write_text(json.dumps(cookies))
                
                # Save analytics
                self._save_analytics(post_url, analytics)
                
                return analytics
                
            finally:
                await browser.close()
    
    async def _scrape_post_data(self, page: Page) -> dict:
        """Scrape engagement metrics from post page"""
        analytics = {
            "scraped_at": datetime.now().isoformat(),
            "post_url": page.url,
            "views": None,
            "reactions": None,
            "comments": None,
            "reposts": None,
            "engagement_rate": None
        }
        
        try:
            # Views (often shown as "X impressions" for your own posts)
            views_selector = "span[data-test-id='social-activity__insights-impression-count']"
            if await page.locator(views_selector).count() > 0:
                views_text = await page.locator(views_selector).inner_text()
                analytics["views"] = self._parse_number(views_text)
            
            # Reactions (likes and other reactions)
            reactions_selector = "button[aria-label*='reaction'] .social-details-social-counts__reactions-count"
            if await page.locator(reactions_selector).count() > 0:
                reactions_text = await page.locator(reactions_selector).inner_text()
                analytics["reactions"] = self._parse_number(reactions_text)
            
            # Comments
            comments_selector = "button[aria-label*='comment'] .social-details-social-counts__comments-count, button[aria-label*='Comment'] span"
            if await page.locator(comments_selector).count() > 0:
                comments_text = await page.locator(comments_selector).first.inner_text()
                analytics["comments"] = self._parse_number(comments_text)
            
            # Reposts (reshares)
            reposts_selector = "button[aria-label*='repost'] .social-details-social-counts__reposts-count"
            if await page.locator(reposts_selector).count() > 0:
                reposts_text = await page.locator(reposts_selector).inner_text()
                analytics["reposts"] = self._parse_number(reposts_text)
            
            # Calculate engagement rate if we have views and interactions
            if analytics["views"] and analytics["views"] > 0:
                interactions = (analytics["reactions"] or 0) + (analytics["comments"] or 0)
                analytics["engagement_rate"] = round((interactions / analytics["views"]) * 100, 2)
            
        except Exception as e:
            analytics["error"] = str(e)
        
        return analytics
    
    def _parse_number(self, text: str) -> int:
        """Parse numbers like '1.2K', '5M' to integers"""
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
        """Save analytics to local JSON file"""
        all_analytics = {}
        if self.analytics_file.exists():
            all_analytics = json.loads(self.analytics_file.read_text())
        
        # Use post URL as key
        post_id = post_url.split("?")[0].split("/")[-1] or post_url
        all_analytics[post_id] = analytics
        
        self.analytics_file.write_text(json.dumps(all_analytics, indent=2))
    
    def get_analytics(self, post_url: str = None) -> dict:
        """Retrieve stored analytics"""
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
        # Retrieve stored analytics
        post_url = sys.argv[2] if len(sys.argv) > 2 else None
        analytics = tool.get_analytics(post_url)
        print(json.dumps(analytics, indent=2))
    else:
        # Scrape new analytics
        post_url = sys.argv[1]
        analytics = await tool.extract_post_analytics(post_url)
        print(json.dumps(analytics, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
