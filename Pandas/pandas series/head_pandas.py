# head() by default it give top 5 values
# tail() by default it give last 5 values

import numpy as np
import pandas as pd

data = [1,5,3,9,15,-1,np.nan]
label = ['a','b','c','d','e','f','g'] # used for the custom indexing
# series_res = pd.Series(data)
series_res = pd.Series(data, index = label)
print(series_res)

# temp = series_res.head(3)
# print(temp)

temp1 = series_res.tail(3)
print(temp1)