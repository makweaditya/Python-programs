# with open("demo.txt", "r") as src:
#     with open("destination.txt", "w") as dest:
#         for line in src:
#             dest.write(line)

with open("destination.txt", "r") as f:
    data = f.read()
    print(data)
print(f.closed)