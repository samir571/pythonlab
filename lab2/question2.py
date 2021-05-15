# WAP which accepts make of four subjects and display total marks, percentage and grade
science = int(input("enter the marks in science"))
math = int(input("enter the marks in math"))
social = int(input("enter the marks in social"))
computer = int(input("enter the marks in computer"))
total_marks = math + social + science + computer
percentage = (total_marks) / 4
print(f" total marks is {total_marks}")
print(f"percentage is {percentage}")
if total_marks >10<30:
    print("failed")
elif total_marks >30<40:
    print("grade C")
elif total_marks >40<50:
    print("grade C+")
elif total_marks >50<60:
    print("grade B")
elif total_marks >60<70:
    print("grade B+")
elif total_marks >70<80:
    print("grade A")
else:
    print("grade A+")
