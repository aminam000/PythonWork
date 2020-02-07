#Warm  Up
weight_in_lbs= float(input("Enter weight in pounds: "))
height_in_in= float(input("Enter height in inches: "))
age= float(input("Enter age in years: "))
gender = input("Enter M if male and F if female: ")
if gender == "M":
    print((66+(6.3* weight_in_lbs) + (12.9*height_in_in) - (6.8*age))/230, "chocolate bars needed to meet calorie needs")
else:
    print((655 +(4.3*weight_in_lbs) + (4.7*height_in_in) - (4.7*age))/230, "chocolate bars needed to meet calorie needs")
