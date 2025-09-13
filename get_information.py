from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome im Headless-Modus starten
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

url = "https://toom.de/p/akku-winkelschleifer-gws-12v-76-professional-12-v-ohne-akku/1501041"
driver.get(url)

wait = WebDriverWait(driver, 15)

# Preis
price_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="buybox-price"]'))
)

# Produktname
productname_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="header-headline"]'))
)

# Beschreibung
description_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="description-accordion"]'))
)

print("Produktname:", productname_element.get_attribute("innerText"))
print("Preis:", price_element.get_attribute("innerText"))
print("Beschreibung:", description_element.get_attribute("innerText"))

driver.quit()
