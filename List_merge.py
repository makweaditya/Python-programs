# Input: two already sorted lists
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Resultant merged list
merged = []

i = 0  # pointer for list1
j = 0  # pointer for list2

# Compare elements and merge
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

# Add remaining elements (if any)
while i < len(list1):
    merged.append(list1[i])
    i += 1

while j < len(list2):
    merged.append(list2[j])
    j += 1

print("Merged Sorted List:", merged)
