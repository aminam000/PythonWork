#fourdigit= (input("Enter a four digit positive number: "))
##print(fourdigit[0])
##print(fourdigit[1])
##print(fourdigit[2])
##print(fourdigit[3])
num= int(input("Enter a four digit positive number: ")) 
ones= num % 10
num = num//10
tens= num%10
num= num//10
hunds= num%10
thous= num//10
print(thous)
print(hunds)
print(tens)
print(ones)
