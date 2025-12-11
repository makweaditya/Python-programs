import pandas as pd
import numpy as np
df3 = pd.DataFrame({
    'City': ['Pune', 'Mumbai', 'Pune', 'Delhi'],
    'Temp': [30, 32, 30, 35]
})
print(df3)
print('------------')
print(df3.replace('Pune', 'PCMC'))
