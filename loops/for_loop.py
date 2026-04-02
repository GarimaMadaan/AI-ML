string = "hello"

#  in is a membership operator that checks if a value is present in a sequence (like a string, list, etc.)
for var in string:
    print(var)  

# if 'o' in string:
#     print("The letter 'o' is present in the string.")

for i in range(5):
    print(i)

word = "artificial intelligence" 

count = 0
for char in word:
    if char in "i":
        count +=1
print("The count of 'i' in the word is:", count)  

count = 0
for char in word:
    if char in "aeiou":
        count +=1
print("The count of vowels in the word is:", count)  