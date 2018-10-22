import math
#please only imput simplified fractions :)
nuMerator = 1
#nuMerator = int(input("what is your numerator? "))
deNominatorOG = int(input("what is your denominator? "))

deNominator = deNominatorOG

nuMbers = []

nonRepeat = 0

while deNominator%2 == 0 or deNominator%5 == 0 or deNominator%10 == 0:
    while deNominator%2 == 0 and deNominator%5 == 0:
        if deNominator%10 == 0:
            deNominator = deNominator/10
            nonRepeat += 1
    if deNominator%5 == 0:
        deNominator = deNominator/5
        nonRepeat += 1
    if deNominator%2 == 0:
        deNominator = deNominator/2
        nonRepeat += 1


print(nonRepeat)

rePeat = 0

aNswer = nuMerator/deNominator

print(aNswer)