import os
import time
import requests
import pandas as pd
from pathlib import Path

from config.settings import STATIC_ROOT
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
    1: ["name", "birth_year", "homeworld", "edited", "films", "height"],
    2: ["name", "residents", "population", "diameter"],
    3: ["title", "director", "release_date"],
    4: ["name", "classification", "people"],
    5: ["name", "cost_in_credits", "max_atmosphering_speed", "films"],
    6: ["name", "cost_in_credits", "max_atmosphering_speed", "hyperdrive_rating", "films"],
}


def handler(category):
    response = requests.get('https://swapi.dev/api/')
    url = response.json().get(category)
    response = requests.get(url)
    return response.json()


def get_data(category, columns=None):
    def add_page(data):
        df = pd.json_normalize(data)
        return pd.concat([result, df[columns]], ignore_index=True)

    if not columns:
        columns = used_cols.get(category)
    result = pd.DataFrame(columns=columns)
    page = handler(CATEGORIES.get(category))

    result = add_page(page.get("results"))

    next_page = page.get("next", None)
    while next_page:
        response = requests.get(next_page)
        result = add_page(response.json().get("results"))
        next_page = response.json().get("next", None)

    # print(result)
    return result


def assign_films(df):
    films = get_data(3, columns=["url", "title"])
    film_dict = {films.loc[i]["url"]: films.loc[i]["title"] for i in range(len(films))}
    for i in range(len(df["films"])):
        df["films"][i] = ", ".join([film_dict.get(film) for film in df["films"][i]])
    return df


def assign_people(df):
    people = get_data(1, columns=["name", "url"])
    people_dict = {people["url"][i]: people["name"][i] for i in range(len(people))}
    for i in range(len(df["people"])):
        df["people"][i] = ", ".join([people_dict.get(resident) for resident in df["people"][i]])


def transform_people(people):
    people['edited'] = pd.to_datetime(people['edited'], errors='coerce',
                                      infer_datetime_format=True).dt.strftime('%Y-%m-%d')
    planets = get_data(2, columns=["name", "url"])
    planets.rename(columns={"name": "pl_name"}, inplace=True)
    people = pd.merge(people, planets, left_on="homeworld", right_on="url")
    people["homeworld"] = people["pl_name"]
    people = people.drop(columns=["pl_name", "url"])

    assign_films(people)
    return people


def transform_planets(planets):
    planets.rename(columns={"residents": "people"}, inplace=True)
    assign_people(planets)
    return planets


def transform_species(species):
    assign_people(species)
    return species


def transform_vehicles(vehicles):
    assign_films(vehicles)
    return vehicles


def transform_starships(starships):
    assign_films(starships)
    return starships


def write_csv(df, category):
    cat_name = CATEGORIES.get(category)
    filename = f'{cat_name}_{int(time.mktime(time.gmtime()))}.csv'
    path = os.path.join(STATIC_ROOT, f'csv/{cat_name}/{filename}')
    # path = Path(f'static/csv/{cat_name}/{filename}')
    df.to_csv(path, index=False)
    models.Collection.objects.create(
        category=category,
        filename=filename,
    )


def get_path(collection):
    cat_name = CATEGORIES.get(collection.category)
    path = os.path.join(STATIC_ROOT,
                        f'csv/{cat_name}/{collection.filename}')
    return path
    # return Path(f'static/csv/{cat_name}/{collection.filename}')
