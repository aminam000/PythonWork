
def h_and_b(weight, height, age, gender):
    if gender == 'F':
        BMR = 655.1+(9.563*weight)+(1.850*height)-(4.676*age)
        round(BMR)
    else:
        BMR = (66.5+13.75*weight)+(5.003*height)-(6.755*age)
        round(BMR)
    return "{0:.2f}".format(BMR)
def r_and_s(weight, height, age, gender):
    if gender == 'F':
        BMR = 447.593+(9.247*weight)+(3.098*height)-(5.677*age)
        round(BMR)
    else:
        BMR = 88.362+(13.397*weight)+(4.799*height)-(5.677*age)
        round(BMR)
    return "{0:.2f}".format(BMR)
def m_and_s(weight,height, age, gender):
    if gender == 'F':
        BMR = (10*weight)+(6.25*height)-(5*age)-161
        round(BMR)
    else:
        BMR = (10*weight)+(6.25*height)-(5*age)+5
        round(BMR)
    return "{0:.2f}".format(BMR)
def convert_pounds_to_kg(pounds):
    kg = (round(pounds/2.205, 2))
    return kg
    
def convert_inches_to_cm(inches):
    cm = (round(inches * 2.54, 2))
    return cm
    
def main():
    weight= float(input("Enter weight in pounds: "))
    mass = convert_pounds_to_kg(weight)
    height= float(input("Enter height in inches: "))
    length = convert_inches_to_cm(height)
    age= int(input("Enter age in years: "))
    gender= input("Enter gender: F/M- ")
    print("Harris and Benedict BMR: ", h_and_b(weight, height, age, gender))
    print("Rosa and Shizgal BMR: " , r_and_s(weight, height, age, gender))
    print("Mifflin and St Jeor BMR: ", m_and_s(weight, height, age, gender))
          
main()
