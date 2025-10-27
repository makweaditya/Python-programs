data = {'a': 10, 'b': 20, 'c': 30}
print(data)
output = {value:key for key,value in data.items()}

print(output)