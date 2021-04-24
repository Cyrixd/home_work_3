import pytest


@pytest.fixture()
def dog_api_url():
    base_url = "https://dog.ceo/api/"
    return base_url


@pytest.fixture()
def by_breed_schema():
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "array",
                        "items": {
                            "type": "string",
                        },
                        },
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }
    return schema


@pytest.fixture(params=[1, 10, 50])
def random_pics_count_valid(request):
    return request.param


@pytest.fixture(params=[51, 100, 1000])
def random_pics_count_invalid(request):
    return request.param


@pytest.fixture(params=["hound", "dingo", "saluki"])
def breed(request):
    return request.param


@pytest.fixture(params=["cat", "pluto", "weedsmoker"])
def breed_nonexistent(request):
    return request.param


@pytest.fixture()
def open_brewery_url():
    base_url = "https://api.openbrewerydb.org/breweries"
    return base_url


@pytest.fixture()
def open_brewery_schema():
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": ["string", "null"]},
                "state": {"type": ["string", "null"]},
                "county_province": {"type": ["string", "null"]},
                "postal_code": {"type": ["string", "null"]},
                "country": {"type": ["string", "null"]},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "updated_at": {"type": ["string", "null"]},
                "created_at": {"type": ["string", "null"]}
            }
        }
    }
    return schema


@pytest.fixture()
def single_brewery_schema():
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {"type": ["string", "null"]},
            "address_2": {"type": ["string", "null"]},
            "address_3": {"type": ["string", "null"]},
            "city": {"type": ["string", "null"]},
            "state": {"type": ["string", "null"]},
            "county_province": {"type": ["string", "null"]},
            "postal_code": {"type": ["string", "null"]},
            "country": {"type": ["string", "null"]},
            "longitude": {"type": ["string", "null"]},
            "latitude": {"type": ["string", "null"]},
            "phone": {"type": ["string", "null"]},
            "website_url": {"type": ["string", "null"]},
            "updated_at": {"type": ["string", "null"]},
            "created_at": {"type": ["string", "null"]}
        }
    }
    return schema


@pytest.fixture(params=[0, 10, 50])
def count_per_page(request):
    return request.param


@pytest.fixture(params=[51, 1000])
def count_per_page_invalid(request):
    return request.param


@pytest.fixture(params=[8034, 8040, 8215, 12010, 14009])
def brewery_id(request):
    return request.param


@pytest.fixture(params=[1, "abc", None])
def brewery_id_invalid(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Tested URL"
    )
    parser.addoption(
        "--status_code",
        default=200,
        help="Required http response status code"
    )
