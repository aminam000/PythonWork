class measure:
    def __init__(self,feet=0,inches = 0):
        self.feet = feet + inches//12
        self.inches = inches % 12
    def __str__(self):
        return measure(self.feet,"'",self.inches,'"')
    def __add__(self,other):
        return measure(self.feet,"'",self.inches,'"')
    def __sub__(self,other):
        inches = self.feet*12 +self.inches
        other_inches = other.feet*12 + other.inches
        return measure(feet = 0, inches =(inches-other_inches))
m1 = measure()
m2 = measure(4,11)
m3 = measure(6,10)

print(m1)
print(m2+m3)
print(m3-m2)


class Vector:

    def __init__(self,lst=[0,0,0]):
        self.vect=lst

    def __str__(self):
        return str(self.vect)

    def __add__(self,other):
        vectlst=[]
        if(len(self.vect)<len(other.vect)):
            for i in range(len(self.vect)):
                vectlst.append(self.vect[i]+other.vect[i])

    elif:
        (len(self.vect)>len(other.vect)):
        for i in range(len(other.vect)):
            vectlst.append(self.vect[i]+other.vect[i])

    else:
        for i in range(len(other.vect)):
            vectlst.append(self.vect[i]+other.vect[i])
    return Vector(vectlst)

    def getValues(self):
        return self.vect

    def setValues(self,lst):
        self.vect=lst

    def __mul__(self,scalar):
        vectlst=[]
        for i in range(len(self.vect)):
            vectlst.append(self.vect[i]*scalar)
        return Vector(vectlst)

    def magnitude(self):
        sum=0
        for i in range(len(self.vect)):
            sum+=self.vect[i]**2
        return math.sqrt(sum) 

v1=Vector([10,20,30])
v2=Vector([5,10,15])
print("First Vector is: ",v1)
print("Second Vector is: ",v2)
print("Magnitude if vector 1 is: ",v1.magnitude())
print("Magnitude if vector 2 is: ",v2.magnitude())
v3=v1+v2
print("The sum of First nad second vector: ",v3)
v3=v1*3
print("Multiply vector 1 by 3 resultant vector is: ",v3)
