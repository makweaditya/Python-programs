import numpy as np
import pandas as pd

data = [1,5,3,9,15,-1,np.nan]
label = ['a','b','c','d','e','f','g'] # used for the custom indexing
# series_res = pd.Series(data)
series_res = pd.Series(data, index = label)
print(series_res)
print("---------------------")
print(f'Print the value of zero th index :{series_res[0]}')
print(f'Print the value of d label :{series_res["d"]}')
print(f'The values from 0th index to 3rd index is : {series_res[0:4]}')
print(f'The values from position a to position c {series_res["a":"c"]}')
# print(series_res[series_res > 10])

