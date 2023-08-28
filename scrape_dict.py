import requests
from bs4 import BeautifulSoup

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Base URL and parameters

# FO-EN = _DictionaryId=2
#base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=2&_SearchFor="

# EN-FO = _DictionaryId=3
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=3&_SearchFor="

# FO-FO = _DictionaryId=1
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=1&_SearchFor="

# DA-FO = _DictionaryId=5
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=5&_SearchFor="

# FO-DA = _DictionaryId=4
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=4&_SearchFor="

# Búsk = _DictionaryId=32
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=32&_SearchFor="

# Nøvn = _DictionaryId=32
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=25&_SearchFor="

# Samheitaorðabók = _DictionaryId=32
# base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=15&_SearchFor="

# Yrkisorðabók = _DictionaryId=32
base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=13&_SearchFor="

end_search = "&_l=fo&_Group="
page_description = "&_DictionaryPage="
page_number = 1

def scrape_page(driver, search_term, page_number):
    url = f"{base_url}{search_term}{page_description}{page_number}"
    driver.get(url)
    time.sleep(2)  # Give the page time to load

    return driver.page_source

def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    words_container = soup.find("div", class_="dictionary-results--words")
    if words_container:
        words = words_container.find_all("div", class_="dictionary-results--word-outer")
        for word in words:
            title_elem = word.find("div", class_="dictionary-results--word-title")
            description_elem = word.find("div", class_="dictionary-results--word-description")

            if title_elem and description_elem:
                title = title_elem.get_text(strip=True)
                description = description_elem.get_text(strip=True)
                yield title, description


#for headless browser use this arguments
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)

# Starts up chrome
# driver = webdriver.Chrome()  

search_terms = "aábdðcefghiíjklmnoópqrstuúvyýæøwxz"
# search_terms = "ghiíjklmnoópqrstuúvyýæøwxz"
#search_terms = "q"

try:
    for term in search_terms:
        with open(f"{term}_words_combined.tsv", "w", encoding="utf-8") as file:
            page_number = 1
            while True:
                html = scrape_page(driver, term, page_number)
                entries = parse_page(html)
                for title, description in entries:
                    file.write(f"{title}\t{description}\n")

                # Check for next button using explicit wait
                try:
                    next_button = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "dictionary-results--pager-item--next"))
                    )
                    if "fal fa-angle-right" in next_button.get_attribute("class"):
                        page_number += 1
                        next_button.click()
                        time.sleep(2)
                    else:
                        break
                except:
                    break  # Exit loop if the next button is not found within the timeout
finally:
    driver.quit()
