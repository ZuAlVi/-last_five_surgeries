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
    if name_key == 'date':
        date = f"{array['date'][8:10]}.{array['date'][5:7]}.{array['date'][:4]}"
        return date
    elif name_key == "description":
        description = array["description"]
        return description
    elif name_key == 'from':
        temp_data = array.get(name_key, 'None').split()
        result = get_from_or_to(temp_data)
        return result
    elif name_key == 'to':
        temp_data = array.get(name_key, 'None').split()
        result = get_from_or_to(temp_data)
        return result
    elif name_key == 'operationAmount':
        temp_amount = array['operationAmount']
        operation_amount = f"{temp_amount.get('amount')} {temp_amount['currency'].get('name')}"
        return operation_amount


def get_from_or_to(data: list) -> str:
    """Функция принимает на вход список с данными
    и возвращает частично закодированную информацию
    о номере карты или счете"""
    card_name = ''
    for part in data:
        if part.isalpha():
            card_name += part + " "
    card_name = card_name.strip()

    if card_name == 'None':
        card_number = ''
    else:
        card_number = data[-1]

    if len(card_number) == 16:
        code_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    elif len(card_number) == 0:
        code_number = ''
    else:
        code_number = f"**{card_number[-4:]}"

    return f'{card_name} {code_number}'


def get_report(date: str, description: str, card_from: str, card_to:str, amount: str) -> str:
    """Функция принимает строковые данные и
    возвращает строку из данных"""
    return f"{date} {description}\n{card_from} -> {card_to}\n{amount}"
