from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# ----------------------------
# Funktion: Produktinfos abrufen
# ----------------------------
def safe_get_element(driver, selector, wait_time=5):
    try:
        wait = WebDriverWait(driver, wait_time)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        return element.get_attribute("innerText")
    except:
        return "Nicht verfügbar"

def get_product_info(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    product_info = {
        "Produktname": safe_get_element(driver, '[data-testid="header-headline"]'),
        "Preis": safe_get_element(driver, '[data-testid="buybox-price"]'),
        "AngebotsPreis": safe_get_element(driver, '[data-testid="price-box-pricing-previous"]'),
        "Beschreibung": safe_get_element(driver, '[data-testid="description-accordion"]'),
        "Gefahrenhinweis": safe_get_element(driver, '[data-testid="safety-advice-accordion"]'),
        "Eigenschaften": safe_get_element(driver, '[data-testid="produktdetails-characteristic-attribute-value"]')
    }

    driver.quit()

    # Dictionary → JSON-String
    product_info_json = json.dumps(product_info, ensure_ascii=False, indent=2)

    print(product_info_json)
    return product_info_json


print(get_product_info(url="https://toom.de/p/pinienrinde-7-15-mm-60-l/4530045"))
