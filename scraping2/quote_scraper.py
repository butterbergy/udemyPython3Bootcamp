import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = "http://quotes.toscrape.com"
url = f"{base_url}/page/1/"
all_quotes = []

while url:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_="quote")
    print("Scraping " + url)
    for quote in quotes:
        text = quote.find(class_="text").get_text()
        author = quote.find(class_="author").get_text()
        bio_link = quote.find("a")["href"]
        all_quotes.append({"text": text, "author": author, "bio_link": bio_link})
    next_btn = soup.find(class_="next")
    url = f"{base_url}{next_btn.find('a')['href']}" if next_btn else None
    # Sleep to be polite scraping the website
    sleep(2)

print(all_quotes)
