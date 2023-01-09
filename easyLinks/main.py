import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ['TOKEN']

def main():
    link = input('Your link: ')

    if is_bitlink(link):
        try:
            click_count = count_clicks(link)
        except requests.exceptions.HTTPError:
            print("Can't find number of clicks for this link(")
            exit()
        print(f'This link has {click_count} clicks')

    else:
        try:
            bitlink = shorten_link(link)
        except requests.exceptions.HTTPError:
            print("Link is invalid. ")
            exit()

        print('Bitlink: ', bitlink)


def shorten_link(link):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "long_url": link,
    }

    bitlink = requests.post(url, json=data, headers=headers)
    bitlink.raise_for_status()
    return bitlink.json()['link']


def count_clicks(bitlink):
    bitlink = bitlink.split("//")[1] if '//' in bitlink else bitlink

    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "unit": "day",
        "units": -1,
    }

    clicks = requests.get(url, params=params, headers=headers)
    clicks.raise_for_status()
    return clicks.json()["total_clicks"]


def is_bitlink(link):
    link = link.split("//")[1] if '//' in link else link
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"

    clicks = requests.get(url, headers=headers)
    return True if clicks.ok else False

main()
