def subtractWhile(total,num,times):
    while times > 0:
        value = total - (num * times)
        print(value)

 
def main():
        total = float(input("Enter a the current total: "))
        num = float(input("What number will be subtracted? "))
        times = float(input("How many times should we subtract? "))
        newestvalue= total - (num * times)
        print("Answer: ", newestvalue)
        
main()
