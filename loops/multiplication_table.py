number = int(input("Enter a number to print its multiplication table: "))

count = 1
while count <= 10:
    print(f"{number} x {count} = {number * count}")
    count += 1