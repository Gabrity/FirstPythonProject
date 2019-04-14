from xlrd import open_workbook


class Instrument:
    IdNumber = 0
    InstrumentName_14 = ""
    PositionInstrumentCIC_12 = ""
    PortfolioCurrency_4 = ""
    QuotationCurrency_21 = ""
    PositionValueQc_22 = 0.0

    def __init__(self, id_number, instrument_string):
        IdNumber = id_number
        InstrumentName_14 = instrument_string[14]
        PositionInstrumentCIC_12 = instrument_string[12]
        PortfolioCurrency_4 = instrument_string[3]
        QuotationCurrency_21 = instrument_string[22]
        PositionValueQc_22 = instrument_string[23]


def read_excel_input():
    # todo make this relative path
    file = "C:\Work\Other_Projects\FirstPythonProject\\resources\SampleTPTReport.xlsx"

    sheet = get_sheet(file)

    instruments = []
    for row in range(1, sheet.nrows):
        line = get_line(row, sheet)
        instrument = Instrument(row, line)
        instruments.append(instrument)
    print(instruments)
    return instruments


def get_sheet(file):
    wb = open_workbook(file)
    if wb.nsheets > 1:
        raise ValueError('We expect a single sheet only')
    sheet = wb.sheets()[0]
    return sheet


def get_line(row, sheet):
    line = []
    for column in range(sheet.ncols):
        value = sheet.cell(row, column)
        line.append(value)
    return line
