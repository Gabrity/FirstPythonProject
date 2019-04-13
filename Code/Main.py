import pandas as pd

#todo make this relative path
file = "C:\Work\Other_Projects\FirstPythonProject\Resources\SampleTPTReport.xlsx"

data = pd.read_excel(file)

print(data)


