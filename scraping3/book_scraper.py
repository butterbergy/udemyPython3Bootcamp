import sqlite3
import requests
from bs4 import BeautifulSoup


def get_title(book):
    return book.find("h3").find("a")["title"]


def get_rating(book):
    par = book.select(".star-rating")
    rating = par[0].get_attribute_list("class")[1]
    ratings = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return ratings[rating]


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("£", "").replace("Â", ""))


def scrape_books(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        title = get_title(book)
        price = get_price(book)
        rating = get_rating(book)
        book_data = (title, price, rating)
        all_books.append(book_data)
    return all_books


def save_data(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE books
        (title TEXT, price REAL, rating INTEGER)''')
    c.executemany("INSERT INTO books VALUES (?,?,?)", all_books)
    connection.commit()
    connection.close()

url = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
all_books = scrape_books(url)
save_data(all_books)
