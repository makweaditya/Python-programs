num = 2
count = 0

for i in range(2,num):
    if (num % i == 0):
        count +=1
if count > 0:
    print('number is not prime')
else:
    print('number is prime')
