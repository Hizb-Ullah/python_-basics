name=input("Enter your name:")
print("Enter the maks of five subjects:")
subject1=float(input("Subject 1:"))
subject2=float(input("Subject 2:"))
subject3=float(input("Subject 3:"))
subject4=float(input("Subject 4:"))
subject5=float(input("Subject 5:"))
total_marks=subject1+subject2+subject3+subject4+subject5
average_marks=total_marks/5
percentage=(total_marks/500)*100
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"
print("======result card======")
print(f"Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Percentage: {percentage}%")  
print(f"Grade: {grade}")
print("++++++++++++Report Card++++++++++++")

