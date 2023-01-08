import requests

location = input('Location: ')
url = f"https://wttr.in/{location}?nMTq&lang=ru"

response = requests.get(url)
response.raise_for_status()
print(response.text)

