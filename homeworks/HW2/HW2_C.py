def forecast():
    temp = float(input("What is the temperature? "))
    if temp > 70:
        wind = float(input("What is the wind speed? "))
        if wind > 2:
            air_pressure = float(input("What is the air pressure? "))
            if air_pressure > 26:
                print("Yes it will rain")
            else:
                print("No it will not rain")
        else:
            print("No it will not rain")
    else:
        wind2 = float(input("What is the wind speed? "))
        if wind2 > 4.5:
            air_pressure2 = float(input("What is the air pressure? "))
            if air_pressure2 > 31:
                print("Yes it will rain")
            else:
                print("No it will not rain")
        else:
            print("No it will not rain")
