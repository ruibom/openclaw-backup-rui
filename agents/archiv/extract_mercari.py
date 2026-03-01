import asyncio
from playwright.async_api import async_playwright
import json
import sys

async def extract_mercari(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until='networkidle', timeout=60000) # Increased timeout to 60 seconds
        
        # Wait for content to load - adjust selectors as per actual Mercari structure
        # The given AGENTS.md had .Heading and [class*="Price"], [class*="description"]
        # It's possible these class names change, so I'll try with a more generic wait.
        # Let's try to wait for an element that typically contains the item title.
        await page.wait_for_selector('h1', timeout=15000) # Assuming product title is typically an h1
        
        # Extract fields
        title = await page.text_content('h1')
        # Price and description selectors might be specific, I'll use the ones from AGENTS.md
        price = await page.text_content('[class*="Price"]') if await page.query_selector('[class*="Price"]') else "N/A"
        description = await page.text_content('[class*="description"]') if await page.query_selector('[class*="description"]') else "N/A"
        
        # Get all images
        images = await page.query_selector_all('img[alt*="product"]')
        image_urls = [await img.get_attribute('src') for img in images] if images else []
        
        await browser.close()
        return {
            'title': title.strip() if title else "N/A",
            'price': price.strip() if price else "N/A",
            'description': description.strip() if description else "N/A",
            'images': image_urls
        }

if __name__ == "__main__":
    url = sys.argv[1]
    result = asyncio.run(extract_mercari(url))
    print(json.dumps(result))
