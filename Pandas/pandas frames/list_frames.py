
import pandas as pd
list = [[1, "A"], [2, "B"], [3, "C"]]
#          0         1          2
# 0 : [1, "A"]
# 1: [2, "B"]
# 2: [3, "C"]


df1 = pd.DataFrame(list, columns=["ID", "Code"])
df2 = pd.DataFrame(list)
print(df1)
print('----------------')
print(df2)
