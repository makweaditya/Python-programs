text = "hello world 123"
print("Original String:", text)


# isalpha() -> checks if all characters are alphabets (no digits/spaces allowed)
alpha_text = "HelloWorld"
print("\n) isalpha() on 'HelloWorld':", alpha_text.isalpha())
print("   isalpha() on original text:", text.isalpha())

# 1isdigit() -> checks if all characters are digits
num_text = "12345"
print("\n) isdigit() on '12345':", num_text.isdigit())
print("    isdigit() on original text:", text.isdigit())

# islower() -> checks if all characters are lowercase
print("\n) islower() on original text:", text.islower())
mixed_text = "Hello"
print("    islower() on 'Hello':", mixed_text.islower())

# isupper() -> checks if all characters are uppercase
upper_text = "HELLO"
print("\n) isupper() on 'HELLO':", upper_text.isupper())
print("    isupper() on original text:", text.isupper())

# swapcase() -> converts upper->lower and lower->upper
print("\n) swapcase():", "HeLLo WoRLd".swapcase())

# isspace() -> checks if string contains only spaces
space_text = "   "
print("\n) isspace() on '   ':", space_text.isspace())
print("    isspace() on original text:", text.isspace())

# lstrip() -> removes leading spaces
strip_text = "   hello   "
print("\n) lstrip() before:", repr(strip_text))
print("    lstrip() after:", repr(strip_text.lstrip()))

# rstrip() -> removes trailing spaces
print("\n) rstrip() before:", repr(strip_text))
print("    rstrip() after:", repr(strip_text.rstrip()))

# replace() -> replaces all occurrences of substring
print("\n) replace('world', 'Python'):", text.replace("world", "Python"))

# join() -> joins elements of a list with a separator
words = ['apple', 'banana', 'cherry']
print("\n) join():", ", ".join(words))