
import pandas as pd
list = [[1, "A"], [2, "B"], [3, "C"]]
df = pd.DataFrame( list, columns=["ID", "Code"])
print(df)
print(type(df))
