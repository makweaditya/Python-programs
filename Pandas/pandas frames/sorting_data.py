import pandas as pd
df4 = pd.DataFrame({
    'Name': ['Ram', 'Shyam', 'Amit', 'John'],
    'Marks': [88, 92, 75, 90]
})
print(df4)
print('--------')
print(df4.sort_values(by='Marks'))
print(df4.sort_values(by='Marks',ascending = False))
