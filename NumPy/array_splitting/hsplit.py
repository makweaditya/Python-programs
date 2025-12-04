import numpy as np

arr1 = np.random.randint(1,15,(4,4))

print(arr1)

sub_arr1,sub_arr2,sub_arr3,sub_arr4 = np.hsplit(arr1,4)

print(f'First subarray is : {sub_arr1}')

print(f'Second subarray is : {sub_arr2}')

print(f'Third subarray is : {sub_arr3}')

print(f'Fourth subarray is : {sub_arr4}')
