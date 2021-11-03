print("Enter the calue of sidesA,B,C")
A = float(input("A:"))
B = float(input("B:"))
C = float(input("C:"))
if A<=0 or B<=0 or C<=0:
    print("Impossible")
else:
    if A == B == C:
        print("Equilateral")
    elif A + B <= C or B + C <= A or A + C <= B:
        print("Impossible")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
         print("Scalene")
