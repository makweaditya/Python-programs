#Linear Search

length = int(input(f"enter number of elements you want to enter in a list"))

l = []

for i in range(0,length):
    num = int(input(f"enter elements {i + 1} in list "))
    l.append(num)

print(l)

search_num = int(input("enter the number you want to seach"))
flag = 0
for j in l:
    if j == search_num:
        flag = 1

if flag == 0:
    print(f"{search_num} is not in list")
else:
    print(f"{search_num} is in list")