import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

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
    # sleep(2)

quote = choice(all_quotes)
print("Here's a quote: ")
print(quote["text"])
remaining_guesses = 4
guess = ''
print(quote["author"])
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(f"Who said this quote?: Guesses Remaining {remaining_guesses}\n")
    if guess.lower() == quote['author'].lower():
        print("YAY YOU WON!!!!")
        break
    remaining_guesses -= 1
    if remaining_guesses == 3:
        response = requests.get(f"{base_url}{quote['bio_link']}")
        soup = BeautifulSoup(response.text, 'html.parser')
        birthdate = soup.find(class_="author-born-date").get_text()
        birthplace = soup.find(class_="author-born-location").get_text()
        print(f"The author was born on {birthdate} {birthplace}")
    elif remaining_guesses == 2:
        print(f"The author's first name starts with {quote['author'][0]}")
    elif remaining_guesses == 1:
        lastname = quote["author"].split()[1]
        print(f"The author's last name starts with {lastname[0]}")
    else:
        print("Sorry you ran out of guesses!")
        print(f"The quote was from {quote['author']}")
