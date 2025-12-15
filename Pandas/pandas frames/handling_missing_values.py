import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 5, 4],
    'B': [5, None, 7, 8],
    'C': ['x', None, 'y', 'z']
})
print(df)
print(df.isnull())
# print(df.isnull().sum())
# print(df.dropna())
# print(df.dropna(axis=1))

print(df.fillna(0))