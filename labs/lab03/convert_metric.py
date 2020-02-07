done = False
while done == False:
    measurement= float(input("Enter value: "))
    metric_value= input("Enter units (centimeters, kilometer, grams, kilos): ")
    centimeters = "centimeters"
    kilos = "kilos"
    grams = "grams"
    kilometers = "kilometers"
    if metric_value == centimeters:
        print ((measurement/2.54), "inches")
    elif metric_value == kilos:
        print ((measurement*2.205), "pounds")
    elif metric_value == grams:
        print ((measurement/28.35), "ounces")
    else:
        print((measurement/1.609), "miles")
    prompt = input("Do you wish to continue? Y/N ")
    if prompt == "N":
        done = True
        



