# Test 3: getting info from Excel
import pandas as pd
import openpyxl
data = pd.read_excel("test.xlsx")
print(data)

# from openpyxl import load_workbook
# data = load_workbook(filename="test.xlsx")
# sheet = data.active
# for name in sheet["B"]:
    # num = name.row
    # if name == "Sapp":
    #     sheet[f"B{num}"] = "Sapp family"
    # else:
    #     sheet[f"B{num}"] = "Not Sapp family"
# data.save("test.xlsx")

