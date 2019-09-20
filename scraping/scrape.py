import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text, "html.parser")
# Get all of the base articles
articles = soup.find_all("article")

with open("rithm_blog.csv", 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["TITLE", "LINK", "DATE"])
    # Extract the title, link, and date from the article
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        href = a_tag["href"]
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, href, date])
