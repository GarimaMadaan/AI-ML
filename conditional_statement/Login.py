username = input("Enter your username: ")
password = input("Enter your password: ")

# if(username == "admin" and password == "pass"):
#     print("Login successful")
# elif(username != "admin"):
#     print("Invalid username")
# else:
#     print("Invalid password")


# nested if statement
if (username == "admin" and password == "pass"):
    print("Login successful")
else:
    if(username !="admin"):
        print("Invalid username")
    else:
        print("Invalid password")