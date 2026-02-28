
import asyncio
from playwright.async_api import async_playwright
import json
import sys

async def extract_mercari(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(url, wait_until='domcontentloaded')
        await page.wait_for_timeout(3000) # 3 second wait
        
        extracted_data = {}
        
        try:
            # Title: "Cedar Ball with Roof ②"
            title_element = await page.query_selector("h1:has-text('Cedar Ball with Roof ②')")
            if not title_element:
                title_element = await page.query_selector("h2:has-text('Cedar Ball with Roof ②')")
            if not title_element: 
                title_element = await page.query_selector("strong:has-text('Cedar Ball with Roof ②')")
            
            if title_element:
                extracted_data['title'] = (await title_element.text_content()).strip()
            else:
                extracted_data['title'] = "Not Found"
        except Exception as e:
            extracted_data['title'] = "Error extracting title"
            print(f"Error extracting title: {e}", file=sys.stderr)

        try:
            # Price: "¥9,000 (incl. tax, shipping included)"
            price_element = await page.query_selector("div:has-text('¥9,000')")
            if not price_element:
                price_element = await page.query_selector("span:has-text('¥9,000')")
            
            if price_element and "(incl. tax, shipping included)" in (await price_element.text_content()):
                extracted_data['price'] = (await price_element.text_content()).strip()
            elif price_element:
                extracted_data['price'] = (await price_element.text_content()).strip()
            else:
                extracted_data['price'] = "Not Found"
        except Exception as e:
            extracted_data['price'] = "Error extracting price"
            print(f"Error extracting price: {e}", file=sys.stderr)

        try:
            # Category: "Furniture / Interior > Interior Accessories > Others"
            category_label = await page.query_selector("dt:text('Category')")
            if category_label:
                category_dd = await category_label.evaluate_handle('(el) => el.nextElementSibling')
                if category_dd:
                    full_category_text = (await category_dd.text_content()).strip()
                    if "Furniture / Interior > Interior Accessories > Others" in full_category_text:
                        extracted_data['category'] = full_category_text
                    else:
                        extracted_data['category'] = "Not Found"
                else:
                    extracted_data['category'] = "Not Found"
            else:
                extracted_data['category'] = "Not Found"
        except Exception as e:
            extracted_data['category'] = "Error extracting category"
            print(f"Error extracting category: {e}", file=sys.stderr)

        try:
            # Condition: "New"
            condition_label = await page.query_selector("dt:text('Condition')")
            if condition_label:
                condition_dd = await condition_label.evaluate_handle('(el) => el.nextElementSibling')
                if condition_dd:
                    full_condition_text = (await condition_dd.text_content()).strip()
                    if "New" in full_condition_text:
                        extracted_data['condition'] = full_condition_text
                    else:
                        extracted_data['condition'] = "Not Found"
                else:
                    extracted_data['condition'] = "Not Found"
            else:
                extracted_data['condition'] = "Not Found"
        except Exception as e:
            extracted_data['condition'] = "Error extracting condition"
            print(f"Error extracting condition: {e}", file=sys.stderr)

        try:
            # Description: "Sugi-dama (cedar ball) handmade in Tottori from local cedar, takes 3 days to make. Set includes roof. Ball size ~26cm."
            desc_element = await page.query_selector("div:has-text('Sugi-dama (cedar ball) handmade in Tottori')")
            if not desc_element:
                desc_element = await page.query_selector("p:has-text('Sugi-dama (cedar ball) handmade in Tottori')")
            
            if desc_element:
                extracted_data['description'] = (await desc_element.text_content()).strip()
            else:
                extracted_data['description'] = "Not Found"
        except Exception as e:
            extracted_data['description'] = "Error extracting description"
            print(f"Error extracting description: {e}", file=sys.stderr)

        await browser.close()
        return extracted_data

if __name__ == "__main__":
    url = sys.argv[1]
    result = asyncio.run(extract_mercari(url))
    print(json.dumps(result))
