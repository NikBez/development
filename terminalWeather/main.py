import requests

lang = 'en'
location = input('Location: ')
if location == 'Череповец':
    lang = 'ru'

url = f"https://wttr.in/{location}?nMTq&lang={lang}"

response = requests.get(url)
response.raise_for_status()
print(response.text)
