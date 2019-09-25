import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

msg = "DAD JOKE 3000"
ascii_art = figlet_format(msg)
colored_ascii = colored(ascii_art, "red")
print(colored_ascii)


topic = input("What do you want to hear a joke about? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic})
data = res.json()
if data.get("results"):
    print(f"I found {len(data['results'])} jokes about {topic}, here's one")
    # Pick a random joke from the results and print
    print(choice(data["results"])["joke"])
else:
    print("I didn't find any jokes on that topic")
