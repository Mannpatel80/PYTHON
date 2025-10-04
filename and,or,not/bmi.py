wieght=float(input("entr you wieght"))
hieght=float(input("entr you hieght"))

BMI=wieght/(hieght/100)**2
print("your bmi is",BMI)

if BMI <= 18.4:
    print("your a re underwight")

elif BMI <=24.9:
    print("you are healthey")

elif BMI <=29.9:
    print("you are over wieght")

elif BMI <=34.9:
    print("you are severyly overwight")

elif BMI <=39.9:
    print("you are obese")

else:
    print("your are severly obese")