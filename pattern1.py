n = int(input("Enter the number of rows"))
for i in range(n):
    for j in range(1, i + 2):
        print('*', end=" ")
    print()