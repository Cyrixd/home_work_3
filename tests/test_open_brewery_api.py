import requests
from jsonschema import validate


def test_list_all_breeds(open_brewery_url, open_brewery_schema):
    response = requests.get(open_brewery_url)
    validate(response.json(), open_brewery_schema)


def test_per_page_in_range(open_brewery_url, count_per_page):
    response = requests.get(open_brewery_url + f"?per_page={count_per_page}")
    assert len(response.json()) == count_per_page


def test_per_page_out_of_range(open_brewery_url, count_per_page_invalid):
    response = requests.get(open_brewery_url + f"?per_page={count_per_page_invalid}")
    assert len(response.json()) == 50


def test_get_brewery_positive(open_brewery_url, single_brewery_schema, brewery_id):
    response = requests.get(open_brewery_url + f"/{brewery_id}")
    assert response.status_code == 200
    validate(response.json(), single_brewery_schema)


def test_get_brewery_negative(open_brewery_url, brewery_id_invalid):
    response = requests.get(open_brewery_url + f"/{brewery_id_invalid}")
    assert response.status_code == 404
