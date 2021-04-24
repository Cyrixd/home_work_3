import pytest
import requests


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status_code"))


def test_url(url, status_code):
    response = requests.get(url=url)
    assert response.status_code == status_code
