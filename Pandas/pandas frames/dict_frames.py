import pandas as pd
data = {
    "Name": ["Amit", "Riya", "John"],
    "Age": [21, 22, 23],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)
print(type(df))

