import math
# CSCI 1133, Lab Section 008, HW 1, Problem 1A
# Amina_Muumin, muumi002
incidentAngle = float (input("Input the incident angle in degrees: "))
incidentAngle = math.radians(incidentAngle)
n1 = float (input("Input the index of refraction of first medium: "))
n2 = float (input("Input the index of refraction of second medium: "))
angleOfRefraction = math.asin(math.sin(incidentAngle) * n1/n2)
print("The angle of refraction is: ", math.degrees(angleOfRefraction), "degrees")
