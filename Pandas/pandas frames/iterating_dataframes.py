import pandas as pd
Employee = {
    'name':['Anil','sunil','priya','anjali'],
    'salary':[10000,25000,45000,35000],
    'post':['HR','Accounts','Teaching','security']
}
df2 = pd.DataFrame(Employee)
print(df2)


# for index,row in df2.iterrows(): # iterating over rows
#     print(index,':',row)

# for i in df2.index: # iterating over rows
#     print(f'{df2["name"][i]} works in {df2["post"][i]} department')
#
for label,col in df2.items():
    print(label,':',col)




