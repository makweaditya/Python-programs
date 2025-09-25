# String Functions Demonstration

text = "hello world 123"
print("Original String:", text)

# 1. len() -> returns length of the string
print("Length of string:", len(text))

# 2. capitalize() -> capitalizes first character
print("After capitalize():", text.capitalize())

# 3. find() -> returns index of first occurrence (or -1 if not found)
print("Index of 'world':", text.find("world"))
print("Index of 'xyz' (not present):", text.find("xyz"))

# 4. count() -> counts how many times a substring occurs
print("Count of 'l':", text.count("l"))

# 5. endswith() -> checks if string ends with given suffix
print("Ends with '123':", text.endswith("123"))
print("Ends with 'world':", text.endswith("world"))


