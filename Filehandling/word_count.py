with open("demo.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Number of words:", len(words))
