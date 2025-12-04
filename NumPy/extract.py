import numpy as np

arr1 = np.random.randint(1,60,(7,9))

print(arr1)

cond = np.mod(arr1,6) == 0

arr2 = np.extract(cond, arr1)
print("out put is--------------")
print(arr2)

print(cond)