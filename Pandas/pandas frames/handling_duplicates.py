import pandas as pd
import numpy as np
df2 = pd.DataFrame({
    'Name': ['A', 'B', 'B', 'C', 'A'],
    'Marks': [90, 85, 85, 88, 90]
})
print(df2)
print('------------')
print(df2.duplicated())
