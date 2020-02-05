# CSCI 1133, Lab Section XXX, HW 1, Problem 1B
# Amina_Muumin, muumi002
# Program: fahr_to_cel_to_kel.py 
# Purpose: This program takes as input an fahrenheit temperature and calculates 
# the celcius and kelvin tempteratures. If the temperature is less than 
# or equal to 32 degrees fahrenheit is will say it is cold. 
# If above 32 but less than 70 it will say cool. Anything greater than 
# or equal to 20 will be declared warm. The program outputs the 
# temperature in all three scales with cold, cool, or warm. 

print('This program converts fahrenheit temperatures to celsius and kelvin\n') 
Tf = float(input('Please enter the temperature in Fahrenheit: ')) 
Tc = (Tf - 32) * 5/9 
print ('The temperature in Celsius is: ', Tc) 

Tk = (Tf -32)*5/9+ 273.15 
print('The temperature in Kelvin is: ', Tk) 

if Tf <= 32: 
	print('It is cold!') 
elif Tf >32 and Tf < 70: 
	print('It is cool.') 
else: print('It is warm.')
