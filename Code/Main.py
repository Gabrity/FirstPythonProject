from instruments_import import read_excel_input
from calculation_tasks import perform_tasks
from excel_writing import write_data_to_excel


def main():
    instruments = read_excel_input()
    perform_tasks(instruments)
    write_data_to_excel(instruments)


try:
    main()
# Naive assumption is that inputs are correct, and if not, ValueError exception is thrown. Incorrect inputs are not
# handled in a nice way for the sake of simplicity.
except ValueError as error:
    print('Caught this error: ' + repr(error))
