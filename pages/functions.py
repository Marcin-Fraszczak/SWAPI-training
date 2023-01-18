import csv
import requests
from pprint import pprint

from . import models


def handler(pd="pipedream"):
    response = requests.get('https://swapi.dev/api/')
    return response.json()


def get_single_record_api(url):
    response = requests.get(url)
    return response.json()


def write_csv(url):
    response = requests.get(url)
    filename = f"{url.split('/')[-2]}_{url.split('=')[-1]}.csv"
    with open(f'static/csv/{filename}', 'w') as csvfile:
        writer = csv.writer(csvfile)
        headers = (response.json().get("results")[0]).keys()
        writer.writerow(headers)
        for item in response.json().get("results"):
            writer.writerow(item.values())
        models.Page.objects.create(
            url=url,
            next=response.json().get('next'),
            previous=response.json().get('previous'),
            filename=filename,
        )
    return csvfile


def get_page(key):
    url = handler().get(key)
    if '?page=' not in url:
        url += '?page=1'
    try:
        file = models.Page.objects.get(url=url)
    except (models.Page.DoesNotExist, models.Page.MultipleObjectsReturned) as e:
        file = None
    if not file:
        document = write_csv(url)
        # print('document written')
        return document
    else:
        # print('document read')
        try:
            return open(f'static/csv/{file.filename}', mode='r')
        except Exception as e:
            print("Sorry", e)



# Page matching query does not exist.
# https://swapi.dev/api/people/
# {   'count': 82,
#     'next': 'https://swapi.dev/api/people/?page=2',
#     'previous': None,
#     'results': [   {   'birth_year': '19BBY',
#                        'created': '2014-12-09T13:50:51.644000Z',
#                        'edited': '2014-12-20T21:17:56.891000Z',
#                        'eye_color': 'blue',
#                        'films': [   'https://swapi.dev/api/films/1/',
#                                     'https://swapi.dev/api/films/2/',
#                                     'https://swapi.dev/api/films/3/',
#                                     'https://swapi.dev/api/films/6/'],
#                        'gender': 'male',
#                        'hair_color': 'blond',
#                        'height': '172',
#                        'homeworld': 'https://swapi.dev/api/planets/1/',
#                        'mass': '77',
#                        'name': 'Luke Skywalker',
#                        'skin_color': 'fair',
#                        'species': [],
#                        'starships': [   'https://swapi.dev/api/starships/12/',
#                                         'https://swapi.dev/api/starships/22/'],
#                        'url': 'https://swapi.dev/api/people/1/',
#                        'vehicles': [   'https://swapi.dev/api/vehicles/14/',
#                                        'https://swapi.dev/api/vehicles/30/']},
#
