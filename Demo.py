# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     for value in row:
#         print(value, end=" ")
#     print()  # new line after each row
#

nums_input = input("enter nums space seperated").split()
nums = []
for x in nums_input:
    nums.append(int(x))

print(nums)

for n in nums:
    if n % 2 == 0:
        print(n)











