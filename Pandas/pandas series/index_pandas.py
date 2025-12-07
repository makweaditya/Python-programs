# index
import numpy as np
import pandas as pd

data = [1,5,3,9,15,-1,np.nan]
label = ['a','b','c','d','e','f','g'] # used for the custom indexing
# series_res = pd.Series(data)
series_res = pd.Series(data, index = label)
print(series_res)

temp = series_res.index
print(temp)