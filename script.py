import requests

URL = "https://www.google.com"
r = requests.get(URL)
print(r.content)
