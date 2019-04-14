from openpyxl import load_workbook


def write_data_to_excel(instruments):
    file = "..\\resources\SampleTPTReport.xlsx"
    xfile = load_workbook(file)
    sheet = xfile.get_sheet_by_name('Sheet1')

    for instrument in instruments:
        cell = "E" + str(instrument.IdNumber + 1)
        sheet[cell] = instrument.Portfolio_TotalNetAssets_5_output
        cell = "I" + str(instrument.IdNumber + 1)
        sheet[cell] = instrument.Portfolio_TotalNumberOfShares_8b_output
        cell = "J" + str(instrument.IdNumber + 1)
        sheet[cell] = instrument.PortfolioCashPercentage_9_output
    xfile.save(file)

