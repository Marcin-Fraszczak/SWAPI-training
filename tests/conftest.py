import pytest
from django.test import Client
from pages.functions import write_csv, get_path
import pandas as pd


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def fake_df():
    d = {'name': ['test_name_1', 'test_name_2'],
         'col2': ['test_value_1', 'test_value_2']}
    df = pd.DataFrame(data=d)
    return df


@pytest.fixture
def fake_csv(fake_df):
    for i in range(1, 7):
        write_csv(fake_df, i)
