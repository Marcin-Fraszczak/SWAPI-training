import csv
import time

import numpy as np
import requests
from pprint import pprint
import pandas as pd
from pathlib import Path

from . import models

CATEGORIES = {
    1: "people",
    2: "planets",
    3: "films",
    4: "species",
    5: "vehicles",
    6: "starships",
}
used_cols = {
    1: ["name", "birth_year", "homeworld", "edited"],
    2: ["name", "url", "residents"],
}


def handler(category):
    response = requests.get('https://swapi.dev/api/')
    url = response.json().get(category)
    response = requests.get(url)
    return response.json()


def get_data(category):
    def add_page(data):
        df = pd.json_normalize(data)
        return pd.concat([result, df[used_cols.get(category)]])

    result = pd.DataFrame(columns=used_cols.get(category))
    page = handler(CATEGORIES.get(category))
    result = add_page(page.get("results"))
    next_page = page.get("next", None)
    while next_page:
        response = requests.get(next_page)
        result = add_page(response.json().get("results"))
        next_page = response.json().get("next", None)

    # print(result)
    return result


def transform_people(people):
    if not people.shape[0]:
        return pd.DataFrame(columns=used_cols.get(1))

    people['edited'] = pd.to_datetime(people['edited'], errors='coerce',
                                      infer_datetime_format=True).dt.strftime('%Y-%m-%d')
    planets = get_data(2)
    planets.rename(columns={"name": "pl_name"}, inplace=True)
    people = pd.merge(people, planets, left_on="homeworld", right_on="url")
    people["homeworld"] = people["pl_name"]
    people = people.drop(columns=["pl_name", "url", "residents"])

    return people


def write_csv(df, category):
    cat_name = CATEGORIES.get(category)
    filename = f'{cat_name}_{int(time.mktime(time.gmtime()))}.csv'
    path = Path(f'static/csv/{cat_name}/{filename}')
    df.to_csv(path, index=False)
    models.Collection.objects.create(
        category=category,
        filename=filename,
    )


def get_path(collection):
    cat_name = CATEGORIES.get(collection.category)
    return Path(f'static/csv/{cat_name}/{collection.filename}')
