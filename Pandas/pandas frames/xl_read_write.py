import pandas as pd

df = pd.read_excel("students_data.xlsx")
print(df)

df.to_excel("output.xlsx", index=False)
