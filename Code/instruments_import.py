from xlrd import open_workbook


class Instrument:
    IdNumber = 0
    PortfolioID_1 = ""
    Portfolio_SharePrice_8 = 0.0
    InstrumentName_14 = ""
    PositionInstrumentCIC_12 = ""
    PortfolioCurrency_4 = ""
    QuotationCurrency_21 = ""
    PositionValueQc_22 = 0.0

    Portfolio_TotalNetAssets_5_output = 0.0
    Portfolio_TotalNumberOfShares_8b_output = 0.0
    PortfolioCashPercentage_9_output = 0.0

    def __init__(self, id_number, instrument_line):
        self.IdNumber = id_number
        self.PortfolioID_1 = instrument_line[0].value
        self.Portfolio_SharePrice_8 = instrument_line[7].value
        self.InstrumentName_14 = instrument_line[14].value
        self.PositionInstrumentCIC_12 = instrument_line[12].value
        self.PortfolioCurrency_4 = instrument_line[3].value
        self.QuotationCurrency_21 = instrument_line[22].value
        self.PositionValueQc_22 = instrument_line[23].value


def read_excel_input():
    file = "..\\resources\SampleTPTReport.xlsx"

    sheet = get_sheet(file)

    instruments = []
    for row in range(1, sheet.nrows):
        line = get_line(row, sheet)
        instrument = Instrument(row, line)
        instruments.append(instrument)
    return instruments


def get_sheet(file):
    wb = open_workbook(file)
    if wb.nsheets != 1:
        raise ValueError('We expect a single sheet')
    sheet = wb.sheets()[0]
    return sheet


def get_line(row, sheet):
    line = []
    for column in range(sheet.ncols):
        value = sheet.cell(row, column)
        line.append(value)
    return line
