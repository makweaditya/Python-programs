import pandas as pd
Employee = {
    'name':['Anil','sunil','priya','anjali'],
    'salary':[10000,25000,45000,35000],
    'post':['HR','Accounts','Teaching','security'],
}
df2 = pd.DataFrame(Employee)
print(df2)
print('-------------------')
df2['gender'] = ['M','M','F','F'] # Adding column
print(df2)
print('---------------------')
# df2.drop(['gender'], axis =1) # without inplace
# print(df2)

df2.drop(['gender'], axis =1, inplace=True)
print(df2)