import math
#please only imput simplified fractions :)

nuMerator = int(input("what is your numerator? "))
deNominator = int(input("what is your denominator? "))

nuMbers = []


while deNominator%2 == 0 or deNominator%5 == 0 or deNominator%10 == 0
if deNominator%2 == 0:
    deNominator = deNominator/2
    
if deNominator%5 == 0:
    deNominator = deNominator/5
    
if deNominator%10 == 0:
    deNominator = deNominator/10
    
print(deNominator)

