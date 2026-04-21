name=input("enter the name:")
weight=float(input("enter weight in kg:"))
height=float(input("enter height in meters:"))
BMI=weight/(height**2)
if BMI<18.5:
    print(f"{name} is underweight")
elif BMI>=118.5 and BMI<=24.9:
    print(f"{name} is normal weight")
elif BMI>=25 and BMI<=29.9:
    print(f"{name} is overweight")
else:
    print(f"{name} is obese")
  