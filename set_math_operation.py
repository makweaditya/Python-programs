A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# print(A | B)   # Union: {1,2,3,4,5,6}
# print(A & B)   # Intersection: {3,4}
# print(A - B)   # Difference: {1,2}
# print(A ^ B)   # Symmetric Difference: {1,2,5,6}

print(A.isdisjoint(B))
