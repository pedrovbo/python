import openpyxl
import pandas as pd
from pandas import ExcelWriter
from openpyxl.workbook import Workbook

planilha = Workbook()

ws = planilha.active

ws['A1'] = 42

ws.append([1,2,3])

planilha.save("sistema_notas.xlsx")
print(planilha)
