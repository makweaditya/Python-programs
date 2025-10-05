matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     for value in row:
#         print(value, end=" ")
#     print()  # new line after each row
#
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")









