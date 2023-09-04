import json


def open_json(path):
    """Функция получает на вход json файл.
    Возвращает список словарей с данными."""
    with open(path, "r", encoding='utf-8') as file:
        file_json = file.read()
    operations = json.loads(file_json)
    return operations


def sort_by_executed_and_date(array: list) -> dict:
    """Функция получает на вход список словарей.
    Возвращает список словарей с последними пятью
    выполнеными операциями"""
    pass
