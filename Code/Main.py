from instruments_import import read_excel_input
from calculation_tasks import perform_tasks

def main():
    instruments = read_excel_input()
    perform_tasks(instruments)


try:
    main()
# Incorrect inputs are not handled in a nice way for the sake of simplicity. Naive assumption is that inputs are
# correct, and if not, ValueError exception is thrown.
except ValueError as error:
    print('Caught this error: ' + repr(error))
