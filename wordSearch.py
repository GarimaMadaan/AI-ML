line = 1
word = "Python"
with open("sample.txt", "r") as f:
    for data in f:
        if(word in data):
            print(f"Found the {word} in the {line}")
            break
        line += 1