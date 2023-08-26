import requests
from bs4 import BeautifulSoup

# Base URL and parameters
base_url = "URL_OF_THE_DICTIONARY_WEBSITE"
search_terms = "abcdefghijklmnopqrstuvwxyz"

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    words_container = soup.find("div", class_="dictionary-results--words")
    if words_container:
        words = words_container.find_all("div", class_="dictionary-results--word-outer")
        for word in words:
            title = word.find("div", class_="dictionary-results--word-title").get_text(strip=True)
            description = word.find("div", class_="dictionary-results--word-description").get_text(strip=True)
            yield title, description

def main():
    for term in search_terms:
        url = f"{base_url}?SearchFor={term}"
        html = scrape_page(url)
        if html:
            entries = parse_page(html)
            with open(f"{term}_words.tsv", "w", encoding="utf-8") as file:
                for title, description in entries:
                    file.write(f"{title}\t{description}\n")

if __name__ == "__main__":
    main()
