i = 1

while i <= 10:
    if i == 5:
        print("Skipping number 5")
        i += 1
        continue
    if i == 8:
        print("Breaking the loop at number 8")
        break
    print(i)
    i += 1