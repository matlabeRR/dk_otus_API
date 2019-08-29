import pytest


@pytest.fixture(scope="module")
def base_url_test():
    url = 'https://dog.ceo/api/'
    return url


@pytest.fixture
def rand_one_test():
    suf_rnd = 'breeds/image/random'
    return suf_rnd


@pytest.fixture
def all_breeds_test():
    suf_all = 'breeds/list/all'
    return suf_all


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url",
        required=False
    )


@pytest.fixture
def url_hand(request):
    return request.config.getoption("--url")
