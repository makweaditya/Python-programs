# String Functions Demonstration

text = "hello world 123"
# print("Original String:", text)

# # 1. len() -> returns length of the string
# print("Length of string:", len(text))

# # 2. capitalize() -> capitalizes first character
# print("After capitalize():", text.capitalize())
#
# 3. find() -> returns index of first occurrence (or -1 if not found)
# print("Index of 'world':", text.find("world"))
# print("Index of 'xyz' (not present):", text.find("xyz"))
#
# # 4. count() -> counts how many times a substring occurs
# print("Count of 'l':", text.count("l"))
#
# # 5. endswith() -> checks if string ends with given suffix
# print("Ends with '123':", text.endswith("123"))
# print("Ends with 'world':", text.endswith("world"))

# # isalpha() -> checks if all characters are alphabets (no digits/spaces allowed)
# alpha_text = "HelloWorld"
# print("\n) isalpha() on 'HelloWorld':", alpha_text.isalpha())
# print("   isalpha() on original text:", text.isalpha())

# # isdigit() -> checks if all characters are digits
# num_text = "12345"
# print("\n) isdigit() on '12345':", num_text.isdigit())
# print("    isdigit() on original text:", text.isdigit())

# # islower() -> checks if all characters are lowercase
# print("\n) islower() on original text:", text.islower())
# mixed_text = "Hello"
# print("    islower() on 'Hello':", mixed_text.islower())

# # isupper() -> checks if all characters are uppercase
# upper_text = "HELLO"
# print("\n) isupper() on 'HELLO':", upper_text.isupper())
# print("    isupper() on original text:", text.isupper())

# # swapcase() -> converts upper->lower and lower->upper
# print("\n swapcase():", "HeLLo WoRLd".swapcase())

# # isspace() -> checks if string contains only spaces
# space_text = ""
# print("isspace() on '   ':", space_text.isspace())
# print("isspace() on original text:", text.isspace())

# lstrip() -> removes leading spaces
strip_text = "   hello   "
# print("lstrip() before:", repr(strip_text))
# print("lstrip() after:", repr(strip_text.lstrip()))

# # rstrip() -> removes trailing spaces
# print("rstrip() before:", repr(strip_text))
# print("rstrip() after:", repr(strip_text.rstrip()))


# # replace() -> replaces all occurrences of substring
# print("replace('world', 'Python'):", text.replace("world", "Python"))


# join() -> joins elements of a list with a separator
words = ['apple', 'banana', 'cherry']
print("join():", ", ".join(words))