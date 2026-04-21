name=input("Enter employee name:")
hourly_rate=float(input("enter hourly rate:"))
hours_worked=int(input("enter the hours you worked:"))

basic_salery=hourly_rate*hours_worked
bonus=basic_salery*0.1
tax=basic_salery*0.15
net_salery=basic_salery+bonus-tax

print("++++++++SALERY SLIP++++++++++++")
print(f"Employee Name: {name}")
print(f"Hourly Rate: {hourly_rate}")
print(f"Hours Worked: {hours_worked}")
print(f"-------------------------------")
print(f"Basic Salary: {basic_salery}")
print(f"Bonus(10%): {bonus}")
print(f"Tax(15%): {tax}")
print(f"-------------------------------")
print(f"Net Salary: {net_salery}")
print(f"+++++++++++++++++++++++++++++++")
