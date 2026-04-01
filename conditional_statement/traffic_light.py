color = input('Enter the traffic light color (red, yellow, green): ')

if(color == 'red'):
    print("Stop")
elif(color == 'yellow'):
    print("Get ready")
elif(color == 'green'):
    print("Go")
else:
    print("Invalid traffic light color")   

#Match Case  
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic light color")