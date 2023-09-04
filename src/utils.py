import json


def open_json(path):
    """Функция получает на вход json файл.
    Возвращает список словарей с данными."""
    with open(path, "r", encoding='utf-8') as file:
        file_json = file.read()
    operations = json.loads(file_json)
    return operations


def sort_by_executed_and_date(array: list) -> list:
    """Функция получает на вход список словарей.
    Возвращает список словарей с последними пятью
    выполнеными операциями"""
    executed_operation = []
    for item in array:
        if item.get('state') == 'EXECUTED':
            executed_operation.append(item)
    executed_operation.sort(key=lambda x: x['date'], reverse=True)
    if len(executed_operation) > 5:
        five_last_operations = executed_operation[:5]
        return five_last_operations
    else:
        return executed_operation


def get_information(array: dict, name_key: str) -> str:
    """Функция получает на вход словарь и ключ.
    Возвращает нужную информацию в зависимости от ключа."""
