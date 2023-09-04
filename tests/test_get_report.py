from src import utils


def test_get_report():
    assert utils.get_report(
        '20.12.2021', 'Перевод', 'Счет **4535', 'Счет **2312', '34543 руб'
    ) == "20.12.2021 Перевод\nСчет **4535 -> Счет **2312\n34543 руб"
