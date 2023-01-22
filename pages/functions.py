import csv
import time

import requests
from pprint import pprint
import pandas as pd
from pathlib import Path

from . import models


def handler(category):
    response = requests.get('https://swapi.dev/api/')
    url = response.json().get(category)
    response = requests.get(url)
    return response.json()


def get_people():
    def add_page(data):
        df = pd.json_normalize(data)
        df['edited'] = pd.to_datetime(df['edited'], errors='coerce', infer_datetime_format=True).dt.strftime('%Y-%m-%d')
        df = df[["name", "birth_year", "homeworld", "edited"]]
        return pd.concat([people, df])

    people = pd.DataFrame()
    page = handler("people")
    people = add_page(page.get("results"))
    next_page = page.get("next", None)
    while next_page:
        response = requests.get(next_page)
        people = add_page(response.json())
        next_page = response.json().get("next", None)

    planets = get_planets()
    people = pd.merge(people, planets, left_on="homeworld", right_on="url")
    people["homeworld"] = people["name_y"]
    people = people.drop(columns=["name_y", "url"])

    filename = f'{int(time.mktime(time.gmtime()))}_people.csv'
    path = Path(f'static/csv/people/{filename}')
    people.to_csv(path, index=False)
    models.Collection.objects.create(
        category=1,
        filename=filename,
    )


def get_planets():
    def add_page(page):
        df = pd.json_normalize(page)
        df = df[["name", "url"]]
        return pd.concat([planets, df])

    planets = pd.DataFrame(columns=["name", "url"])
    page = handler("planets")
    planets = add_page(page.get("results"))
    next_page = page.get("next", None)
    while next_page:
        response = requests.get(next_page)
        planets = add_page(response.json())
        next_page = response.json().get("next", None)

    return planets
