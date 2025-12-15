import pandas as pd
df = pd.read_csv("students_data.csv")
# print(df)

# Read specific column
temp = pd.read_csv("students_data.csv", usecols=["Name", "Marks"])
print(temp)

df.to_csv("output.csv", index=False)

