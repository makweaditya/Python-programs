str1 = input("Enter a string: ")
i = 0
str2 = ""  # start with empty string

while i < len(str1):
    str2 += str1[(i + 2) % len(str1)]  # build new string by concatenation
    i += 1

print("Original:", str1)
print("Shifted :", str2)