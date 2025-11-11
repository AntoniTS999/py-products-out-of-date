from app.main import outdated_products
from unittest import mock
import pytest
import datetime

@pytest.fixture(scope="function")
def created_products():
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]

@pytest.fixture(scope="function")
def mocked_datetime():
    with mock.patch("app.main.datetime") as mock_date:
        yield mock_date

def test_should_return_product_names(mocked_datetime, created_products):
    mocked_datetime.date.today.return_value = datetime.date.today()
    assert outdated_products(created_products) == ['salmon', 'chicken', 'duck']

def test_should_return_empty_list_if_products_are_not_expired(mocked_datetime, created_products):
    mocked_datetime.date.today.return_value = datetime.date(2022, 1, 1)
    assert outdated_products(created_products) == []

def test_should_return_list_of_names_of_expired_products(mocked_datetime, created_products):
    mocked_datetime.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(created_products) == ["duck"]

