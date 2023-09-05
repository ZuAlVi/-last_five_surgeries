from src.last_five_surgeries.setting import PATH
from src import utils
import json


def main():
    with open(PATH, "r", encoding='utf-8') as file:
        file_json = file.read()
    operations = json.loads(file_json)
    executed_operations = utils.sort_by_executed(operations)
    operations_sort_by_date = utils.sort_by_date(executed_operations)
    last_5_operations = utils.get_last_five_operation(operations_sort_by_date)
    for item in last_5_operations:
        date_operation = utils.get_information(item, 'date')
        operation_descript = utils.get_information(item, "description")
        information_from = utils.get_information(item, 'from')
        information_to = utils.get_information(item, 'to')
        operation_amount = utils.get_information(item, 'operationAmount')
        print(utils.get_report(
            date_operation,
            operation_descript,
            information_from,
            information_to,
            operation_amount)
        )
        print()


if __name__ == '__main__':
    main()
