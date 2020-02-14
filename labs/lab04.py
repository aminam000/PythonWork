#WARM UP

##celcius = 100
##farenheit = int((9/5)* celcius +32)
##while farenheit != celcius:
##    celcius = celcius -1
##    farenheit = int((9/5)* celcius +32)
##print(farenheit)
##print(celcius)

#STRETCH
import math
import random
def estimatePi(sampleSize):
    r = 1
    h= 0
    for i in range(sampleSize):
        x = random.uniform(-1,1)
        y= random.uniform(-1,1)
        if x**2+y**2 <= r**2:
            h = h+1
    pi = h/sampleSize*4
    return pi
           

def main():
    done = False
    while done == False:
        sample = int(input("Enter a sample size:  "))
        print(estimatePi(sample))
        prompt = input("Do you wish to continue? Y/N ")
        if prompt == "N":
            done = True

    
#WORKOUT
##def Take_Away():
##    y = 21
##    prompt = input("Do you want to go first? Y/N ")
##    if prompt == "N":
##        return "Ok"
##    else:
##        done = False
##        while done == False:
##            y > 0
##            x = int(input("Choose a number of objects to take (1,2,3): "))
##            y= y - x
##            print(y)
##            if y == 0:
##                done = True
##                print("You win!")
##                
##    
##    
##            
##
##        
##    
##  
##        
##
