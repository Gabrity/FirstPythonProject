# import pandas as pd
from xlrd import open_workbook


def perform_tasks():
    excel_content = read_excel_input()


def read_excel_input():
    # todo make this relative path
    file = "C:\Work\Other_Projects\FirstPythonProject\Resources\SampleTPTReport.xlsx"

    # data = pd.read_excel(file)
    wb = open_workbook(file)
    if wb.nsheets > 1:
        raise ValueError('We expect a single sheet only')
    for sheet in wb.sheets():
        values = []
        for row in range(sheet.nrows):
            col_value = []
            for col in range(sheet.ncols):
                value = sheet.cell(row, col).value
                try:
                    value = str(int(value))
                except:
                    pass
                col_value.append(value)
            values.append(col_value)
    print(values)
    return values


try:
    perform_tasks()
except ValueError as error:
    print('Caught this error: ' + repr(error))
