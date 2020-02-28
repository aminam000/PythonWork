def CholesterolRatio(total, HDL):
    ratio = (float(total/HDL))
    if ratio <= 3.5:
        risk = "less than average risk"
    if ratio > 3.5 and ratio <=4.5:
        risk = "average risk"
    if ratio > 4.5:
        risk = "high risk"
    nratio = str(ratio)+ ": "+risk
    return nratio

def main():
    total = int(input("Total cholesterol number: "))
    HDL = int(input("HDL number: "))
    print(CholesterolRatio(total, HDL))
