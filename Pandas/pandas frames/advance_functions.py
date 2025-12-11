import pandas as pd
df5 = pd.DataFrame({
    'City': ['Pune', 'Pune', 'Mumbai', 'Mumbai'],
    'Sales': [200, 300, 150, 400]
})
print(df5)

print(df5['Sales'].sum())

print(df5['Sales'].mean())

print(df5['Sales'].count())

print(df5['Sales'].min())

print(df5['Sales'].max())

print(df5['Sales'].std())

print(df5.groupby('City')['Sales'].sum())
