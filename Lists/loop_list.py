num = [1,2,3,4,5]
x = 10
idx = 0

for var in num:
    if(var == x):
        print(f"{x} is found at the index {idx}")
        break
else:
    print(f"{x} is not found in the list")

