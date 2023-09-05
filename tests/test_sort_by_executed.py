from src.utils import sort_by_executed


def test_sort_by_executed(array_fixture):
    assert sort_by_executed(array_fixture) == [
        {"state": "EXECUTED", "date": "2019-08-26T10:50:58.294041"},
        {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"state": "EXECUTED", "date": "2018-01-26T15:40:13.413061"},
        {"state": "EXECUTED", "date": "2018-11-29T07:18:23.941293"},
        {"state": "EXECUTED", "date": "2018-04-14T19:35:28.978265"},
        {"state": "EXECUTED", "date": "2019-09-11T17:30:34.445824"}
    ]
