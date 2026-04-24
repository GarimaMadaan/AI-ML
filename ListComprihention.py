squares = []
for i in range(6):
    squares.append(i**2)
print(squares)

sq = [i*i for i in range(6) if i%2 != 0]
print(sq)

nums = [-2, -4, 3, 5, 2, -1]
positive =[0 if value < 0 else value for value in nums]
print(positive)

words = ["Python", "is", "a", "great", "language"]
words = [val.upper() for val in words]
print(words)