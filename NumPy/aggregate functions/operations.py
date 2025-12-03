import numpy as np


# sum--------------------

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([1,2,3,4,5])
temp = np.sum(a1)
print(f'sum of elements of a1 is :{temp}')
temp2 = np.sum(a2)
print(f'sum of elements of a2 is :{temp2}')
temp3 = temp + temp2
print(temp3)


#product -----------------------

arr = np.array([1, 2, 3, 4])
print(f'The product is : {np.prod(arr)}')


#Mean ------------------------

arr = np.array([2, 4, 6, 8])

print(f'The mean is : {np.mean(arr)}')

# t = np.sum(arr) / len(arr)
# print(t)

# Min and Max------------

arr = np.array([2,5,7,9,11])
print(f'The minimum value in array is : {np.min(arr)}')
print(f'The maximum value in array is : {np.max(arr)}')

# argmin and argmax----------

arr = np.array([2,5,7,9,11])

print(np.argmin(arr))
print(np.argmax(arr))
