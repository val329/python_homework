from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2025/")

results = []

# finding the sibling header element using the id attributes
h2 = driver.find_element(By.CSS_SELECTOR, '[id="top-102025-list"]')

if h2:
    ol = h2.find_element(By.XPATH, 'following-sibling::ol[1]')
    li_entries = ol.find_elements(By.TAG_NAME, 'li')

for item in li_entries:
    links = item.find_elements(By.TAG_NAME, 'a')

    results.append({
        "Title": item.text,
        "Link": links[0].get_attribute("href")
    })

print(results)


# Save data to CSV 
with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for line in results:
        writer.writerow([line["Title"], line["Link"]])


driver.quit()