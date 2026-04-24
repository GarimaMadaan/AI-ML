# f = open("sample.txt", "r")

# data = f.read()
# print(data)

# data = f.readline()
# print(data)
# f.close()

# open("sample.txt", "w").write("This is a new line.\n")

f = open("sample.txt", "r+")
f.write(123)
f.read()

f.close()
