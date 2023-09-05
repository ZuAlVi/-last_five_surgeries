from src.last_five_surgeries.setting import PATH
from src import utils


def main():
    operations = utils.open_json(PATH)
    last_5_operations = utils.sort_by_executed_and_date(operations)
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
