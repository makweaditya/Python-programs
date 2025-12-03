import numpy as np

no_rows = int(input("Enter number of rows"))
no_columns = int(input("Enter number of columns"))

array1 = np.random.randint(10,20, (no_rows,no_columns))

# array2 = array1 + 5

# array2 = np.add(array1,5)
# array3 =np.subtract(array1,1)
# array4 = np.multiply(array1,2)
# array5 = np.divide(array1, 2)
# array6 = np.remainder(array1, 2)
array7 = np.power(array1,2)


print(f'Before addition {array1}')
# print(f'After addition {array2}')
# print(f'After subtraction {array3}')
# print(f'After multiplication {array4}')
# print(f'After division {array5}')
# print(f'After division the remainders are : {array6}')
print(f'After power : {array7}')