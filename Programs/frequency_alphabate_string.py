# Program to count frequency of alphabets in a string

text = input("Enter a string: ")

# Convert to lowercase to ignore case difference
text = text.lower()

# Create empty lists
alphabets = []
freq = []

# Loop through each character
for ch in text:
    if ch.isalpha():  # Check if it's an alphabet
        if ch in alphabets:
            index = alphabets.index(ch)
            freq[index] += 1
        else:
            alphabets.append(ch)
            freq.append(1)

# Display the frequency
print("\nAlphabet Frequency:")
for i in range(len(alphabets)):
    print(alphabets[i], ":", freq[i])
