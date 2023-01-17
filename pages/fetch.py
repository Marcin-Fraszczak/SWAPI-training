from pprint import pprint

import requests


def handler(pd="pipedream"):
    response = requests.get('https://swapi.dev/api/')
    # pprint(response.json().get("people"), indent=4)
    # pprint(response.json().keys(), indent=4)
    return response.json()


def get_data(key):
    url = handler().get(key)
    response = requests.get(url)
    # response = requests.get(url+f"?page={page}")
    return response.json().get("results")


def get_single_record(url):
    response = requests.get(url)
    # pprint(response.json(), indent=4)
    return response.json()
