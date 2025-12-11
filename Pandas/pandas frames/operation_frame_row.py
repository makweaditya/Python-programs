import pandas as pd
Employee = {
    'name':['Anil','sunil','priya','anjali'],
    'salary':[10000,25000,45000,35000],
    'post':['HR','Accounts','Teaching','security']
}
df2 = pd.DataFrame(Employee)
print(df2)
print('---------------')
df3 = pd.DataFrame([['Ram',50000,'security']],columns=['name','salary','post'])
print(df3)
print('----------------------')
df2 = pd.concat([df2,df3])
#
print(df2)
print('--------------')
df2.drop([0], axis =0, inplace=True)
print(df2)