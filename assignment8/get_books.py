from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
import json


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

# finding the li elements using the id attributes
li_entries = driver.find_elements(By.CSS_SELECTOR, '[data-test-id="searchResultItem"]')  

results = []
row = {}

# iterating through the list of books and finding the title, authos and format/year
for book in li_entries:

    try:    
        row["Title"] = book.find_elements(By.CSS_SELECTOR, "span.title-content")[0].text
    except:
        row["Title"] = ""

    try:
        authors_list = book.find_elements(By.CSS_SELECTOR, "span.cp-author-link")
        row["Author"] = ";".join([a.text for a in authors_list])
    except:
        row["Author"] = ""

    try:
        format_section = book.find_element(By.CSS_SELECTOR, "div.manifestation-item-format-info-wrap")
        row["Format-Year"] = format_section.find_elements(By.CSS_SELECTOR, "span.cp-screen-reader-message")[0].text
    except:
        row["Format-Year"] = ""

    results.append(row)
    row = {}
    

df = pd.DataFrame(results)
print(df)


# saving data to CSV
with open("get_books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Format-Year"])
    for line in results:
        writer.writerow([line["Title"], line["Author"], line["Format-Year"]])


# saving data to JSON
data = {"links": results}
with open("get_books.json", "w") as json_file:
    json.dump(data, json_file, indent=4)


driver.quit()
