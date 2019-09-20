import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = f"{BASE_URL}/page/1/"
    while url:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        print("Scraping " + url)
        for quote in quotes:
            text = quote.find(class_="text").get_text()
            author = quote.find(class_="author").get_text()
            bio_link = quote.find("a")["href"]
            all_quotes.append(
                {"text": text, "author": author, "bio_link": bio_link})
        next_btn = soup.find(class_="next")
        url = f"{BASE_URL}{next_btn.find('a')['href']}" if next_btn else None
        # Sleep to be polite scraping the website
        # sleep(2)
    return all_quotes


def write_quotes(quotes):
    with open("quotes.csv", 'w') as file:
        headers = ["text", "author", "bio_link"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)
