from src.utils import get_information
import pytest


@pytest.mark.parametrize('array, name_key, expected', [
    ({'date': "2019-08-26T10:50:58.294041"}, 'date', '26.08.2019'),
    ({'description': "Перевод организации"}, "description", "Перевод организации"),
    ({'from': "Visa Classic 1596837868705199"}, 'from', 'Visa Classic 1596 83** **** 5199'),
    ({}, 'from', 'None '),
    ({'to': "Счет 15968378687051993433546"}, 'to', 'Счет **3546'),
    ({"operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }}}, 'operationAmount', '8221.37 USD'),
])
def test_get_information(array: dict, name_key: str, expected):
    assert get_information(array, name_key) == expected
