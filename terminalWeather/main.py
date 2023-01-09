import requests

locations = ('London', 'SVO', 'Cherepovets')

params = {
    "nMTq": "",
    "lang": "ru"
}

for loc in locations:
    url = f"https://wttr.in/{loc}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
