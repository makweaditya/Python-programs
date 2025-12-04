import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[4, 5, 6],[7,8,9]])
print(a)
print(b)
result = np.hstack((a, b))
print("output is:")
print(result)

#####################################

# arr1 = np.random.randint(1,20,15)
# arr2 = np.random.randint(5,25,15)
#
# print(arr1)
# print(arr2)

# result = np.hstack((arr1,arr2))
#
# print(result)