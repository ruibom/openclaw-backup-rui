
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mercari_url = "https://jp.mercari.com/en/item/m76818888420?utm_source=ios&utm_medium=share&source_location=share"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

try:
    driver.get(mercari_url)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Heading")))

    title = driver.find_element(By.CSS_SELECTOR, ".Heading").text
    price = driver.find_element(By.CSS_SELECTOR, '[class*="Price"]').text
    description = driver.find_element(By.CSS_SELECTOR, '[class*="description"]').text

    # Extracting images
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img[alt*="product"]')
    image_urls = [img.get_attribute('src') for img in image_elements]

    product_data = {
        "title": title,
        "price": price,
        "description": description,
        "images": image_urls,
        "source_url": mercari_url
    }
    print(json.dumps(product_data))

except Exception as e:
    print(json.dumps({"error": str(e)}))
finally:
    driver.quit()
