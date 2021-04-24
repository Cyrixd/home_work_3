import pytest
import requests
from jsonschema import validate


@pytest.fixture()
def json_ph_url():
    return "https://jsonplaceholder.typicode.com/"


@pytest.fixture()
def post_schema():
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": ["number", "string"]},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        }
    }
    return schema


@pytest.fixture()
def photos_schema():
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "albumId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "url": {"type": "string"},
                "thumbnailUrl": {"type": "string"},
            }
        }
    }
    return schema


@pytest.fixture(params=[1, 10, 100])
def post_id(request):
    return request.param


@pytest.fixture(params=[7, 666, 42])
def new_post(request):
    post = {
        "title": "foo",
        "body": "bar",
        "userId": request.param
    }
    return post


def test_get_post_by_id(json_ph_url, post_id, post_schema):
    response = requests.get(json_ph_url + f"posts/{post_id}")
    validate(response.json(), post_schema)


def test_post_new_posts(json_ph_url, new_post, post_schema):
    response = requests.post(json_ph_url + f"posts", data=new_post)
    assert response.status_code == 201
    validate(response.json(), post_schema)
    assert int(response.json()["userId"]) == new_post["userId"]


def test_del_post(json_ph_url):
    response = requests.delete(json_ph_url + f"posts/1")
    assert response.status_code == 200
    assert response.json() == {}


def test_get_all_photos(json_ph_url, photos_schema):
    response = requests.get(json_ph_url + f"photos")
    validate(response.json(), photos_schema)


def test_get_all_photos_max_count(json_ph_url):
    response = requests.get(json_ph_url + f"photos")
    assert len(response.json()) == 5000
