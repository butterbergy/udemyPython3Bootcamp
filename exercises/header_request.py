import requests
url = "https://icanhazdadjoke.com"
res = requests.get(url, headers={"Accept": "application/json"})
data = res.json()
print(res.text)
print(data)
print(data["joke"])
