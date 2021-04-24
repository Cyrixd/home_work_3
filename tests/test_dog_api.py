import requests
from jsonschema import validate


def test_list_all_breeds(dog_api_url):
    res = requests.get(dog_api_url + "breeds/list/all")
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    validate(res.json(), schema)


def test_image_random_in_range(dog_api_url, random_pics_count_valid):
    result = requests.get(dog_api_url + f"breeds/image/random/{random_pics_count_valid}")
    assert result.status_code == 200
    assert len(result.json()["message"]) == random_pics_count_valid


def test_image_random_out_of_range(dog_api_url, random_pics_count_invalid):
    result = requests.get(dog_api_url + f"breeds/image/random/{random_pics_count_invalid}")
    assert result.status_code == 200
    assert len(result.json()["message"]) == 50


def test_by_breed_positive(dog_api_url, breed, by_breed_schema):
    result = requests.get(dog_api_url + f"breed/{breed}/images")
    assert result.status_code == 200
    validate(result.json(), by_breed_schema)


def test_by_breed_negative(dog_api_url, breed_nonexistent, by_breed_schema):
    result = requests.get(dog_api_url + f"breed/{breed_nonexistent}/images")
    assert result.status_code == 404


