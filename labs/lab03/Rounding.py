def roundFloat(num):
    if num >= 0:
        num = num + 0.5
    else:
        num= num-0.5
    return int(num)
def main():
    anything = float(input("Enter a floating point number: "))
    print("The rounded integer is", roundFloat(anything))
