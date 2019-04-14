from instruments_import import read_excel_input


def perform_tasks():
    instruments = read_excel_input()


try:
    perform_tasks()
except ValueError as error:
    print('Caught this error: ' + repr(error))
