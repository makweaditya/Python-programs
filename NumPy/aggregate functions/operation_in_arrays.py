import numpy as np

no_rows = int(input("Enter number of rows"))
no_columns = int(input("Enter number of columns"))

array1 = np.random.randint(10,20, (no_rows,no_columns))
array2 = np.random.randint(20,30,(no_rows,no_columns))
print(f'array1 is {array1}')
print(f'array2 is {array2}')
# array3 = np.add(array1,array2)
# array3 = np.subtract(array1,array2)
# array3 = np.multiply(array1,array2)
array3 = np.divide(array1,array2)
print(f'after addtion {array3}')

