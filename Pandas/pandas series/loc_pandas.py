# loc, iloc for acessing the data by passing the value of index etc....

import numpy as np
import pandas as pd

data = [1,5,3,9,15,-1,np.nan]
label = ['a','b','c','d','e','f','g'] # used for the custom indexing
# series_res = pd.Series(data)
series_res = pd.Series(data, index = label)
print(series_res)
print("---------------------")
# print(f'Print the value of zero th index :{series_res[0]}')
temp = series_res[1]
print(temp)

temp1 = series_res.iloc[-1]
print(temp1)