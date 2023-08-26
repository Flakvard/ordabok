import requests
from bs4 import BeautifulSoup

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# Base URL and parameters

# FO-FO = _DictionaryId=1

# FO-EN = _DictionaryId=2
#base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=2&_DictionaryPage=1&_SearchFor="

# EN-FO = _DictionaryId=3
base_url = "https://sprotin.fo/dictionaries?_SearchInflections=0&_SearchDescriptions=0&_DictionaryId=3&_DictionaryPage=1&_SearchFor="
search_terms = "aábdðcefghiíjklmnoópqrstuúvyýæøwxz"
#search_terms = "a"

end_search = "&_l=fo&_Group="


def scrape_page(driver, search_term):
    url = f"{base_url}{search_term}{end_search}"
    driver.get(url)
    time.sleep(2)  # Give the page time to load

    return driver.page_source

def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    words_container = soup.find("div", class_="dictionary-results--words")
    if words_container:
        words = words_container.find_all("div", class_="dictionary-results--word-outer")
        for word in words:
            title = word.find("div", class_="dictionary-results--word-title").get_text(strip=True)
            description = word.find("div", class_="dictionary-results--word-description").get_text(strip=True)
            yield title, description


#for headless browser use this arguments
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)

# Starts up chrome
#driver = webdriver.Chrome()  

search_terms = "aábdðcefghiíjklmnoópqrstuúvyýæøwxz"
#search_terms = "a"

try:
    for term in search_terms:
        html = scrape_page(driver, term)
        entries = parse_page(html)
        with open(f"{term}_words.tsv", "w", encoding="utf-8") as file:
            for title, description in entries:
                file.write(f"{title}\t{description}\n")
finally:
    driver.quit()
