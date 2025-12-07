import numpy as np
import pandas as pd

# name = ['Anil','sunil','priya','anjali']
# sereis1 = pd.Series(name)
# print(sereis1)
#
# salary = [10000,25000,45000,35000]
# sereis2 = pd.Series(salary)
#
# post = ['HR','Accounts','Teaching','security']
# sereis3 = pd.Series(post)
#
# df = pd.DataFrame({'Emp_name': name, 'Emp_salary':salary,'Emp_post':post})
# print(df)

Employee = {
    'name':['Anil','sunil','priya','anjali'],
    'salary':[10000,25000,45000,35000],
    'post':['HR','Accounts','Teaching','security']
}
df2 = pd.DataFrame(Employee)
print(df2)

# print(df2['name'])    # accessing by column names
# print(df2 [["name","salary"]])

# print(df2.loc[0])
# print(df2.loc[0:1])

# print(df2.iloc[1])
# print(df2.iloc[0:2])
# print(df2.iloc[0:2] )