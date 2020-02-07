done= False
while done== False:
    m= int(input("Enter a month(3-14): "))
    d= int(input("Enter day: "))
    y= int(input("Enter a year: "))
    zeller= (d + 5 + (26 *(m+1)//10) + ((5*(y%100))//4) + ((21*(y//100))//4))%7
    if zeller == 0:
        zeller = "Monday"
    elif zeller == 1:
        zeller = "Tuesday"
    elif zeller == 2:
        zeller = "Wednesday"
    elif zeller == 3:
        zeller = "Thursday"
    elif zeller == 4:
        zeller = "Friday"
    elif zeller == 5:
        zeller = Saturday
    elif zeller == 6:
        zeller = "Sunday"
    if m ==13 or m == 14:
        m = m - 12
        y = y + 1
    print(m,'/',d,'/',y,'is a', zeller)
    prompt = input("Continue? Y/N ")
    if prompt == "N":
        done = True
            
                                
