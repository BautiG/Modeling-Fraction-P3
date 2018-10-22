import math
#please only imput simplified fractions :)
#program only works if the numerator<denominator 

nuMerator = int(input("what is your numerator? "))
deNominatorOG = int(input("what is your denominator? "))
deNominator = deNominatorOG
print("The decimal equivalent of this fraction is ",+nuMerator/deNominator)

nonRepeating = 0

while deNominator%2 == 0 or deNominator%5 == 0 or deNominator%10 == 0:
    while deNominator%2 == 0 and deNominator%5 == 0:
        if deNominator%10 == 0:
            deNominator = deNominator/10
            nonRepeating += 1
    if deNominator%5 == 0:
        deNominator = deNominator/5
        nonRepeating += 1
    if deNominator%2 == 0:
        deNominator = deNominator/2
        nonRepeating += 1

print("the number of non repeating digits is ",+nonRepeating)

rePeating = 0
nuMbers = []
reMainder = 0
nuMeratorCheck = nuMerator

if nuMerator%deNominator != 0:
    nuMerator = nuMerator*10
    reMainder = nuMerator%deNominator
    nuMbers.append(reMainder)
    rePeating +=1
    while nuMeratorCheck not in nuMbers:
        nuMerator = nuMerator*10
        reMainder = nuMerator%deNominator
        nuMbers.append(reMainder)
        rePeating +=1
        

if reMainder in nuMbers:
    print("the number of repeating digits is ",+rePeating)