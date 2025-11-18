# Program to count frequency of elements in a list (without using map)

# Take input from user
nums = input("Enter numbers separated by space: ").split()

# Convert each input to integer
for i in range(len(nums)):
    nums[i] = int(nums[i])

# Create empty lists
unique = []
freq = []

# Count frequency
for n in nums:
    if n in unique:
        index = unique.index(n)
        freq[index] += 1
    else:
        unique.append(n)
        freq.append(1)

# Display frequency
print("\nFrequency of each element:")
for i in range(len(unique)):
    print(unique[i], ":", freq[i])
