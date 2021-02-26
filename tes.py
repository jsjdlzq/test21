
import pandas
import openpyxl
df = {"name": ["luke"], "age": [12]}
cd = pandas.DataFrame(df)
cd.to_excel("mydata.xlsx")
