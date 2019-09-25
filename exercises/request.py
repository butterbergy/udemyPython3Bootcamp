import requests
url = "https://www.google.com"
response = requests.get(url)
print(response)
print(response.status_code)
