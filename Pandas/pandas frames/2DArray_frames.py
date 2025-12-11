import numpy as np
import pandas as pd

array1 = np.random.randint(1,25,(3,4))
print(array1)
# print(type(array1))

df = pd.DataFrame(array1)
print(df)
print('------------')
df1 = pd.DataFrame(array1,columns=["A", "B","C","D"])
print(df1)