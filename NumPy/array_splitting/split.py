import numpy as np

arr1 = np.random.randint(1,15,(4,4))

print(arr1)

sub_arr1,sub_arr2 = np.split(arr1,2,axis = 1)

print(f'First subarray is : {sub_arr1}')

print(f'Second subarray is : {sub_arr2}')