nums = [1, 2, 2, 3, 4, 4, 5]
output = [n**2 for n in nums]
print(output)
temp = set(output)
print(temp)
# print(f"before comprehension {nums}")
# unique_squares = {n**2 for n in nums}
# print(unique_squares)
