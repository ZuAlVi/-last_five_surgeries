from src.utils import get_last_five_operation


def test_get_last_five_operation(array_fixture, array_fixture_2):
    assert get_last_five_operation(array_fixture) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"state": "EXECUTED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
    ]

    assert get_last_five_operation(array_fixture_2) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
