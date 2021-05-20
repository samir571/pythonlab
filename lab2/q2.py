#WAP which accepts marks of four subjects and display total marks, percentage and grade.Hint: more than 70%–>distinction, more than 60%–>first, more than 40%–>pass, less than 40%–>fail
sub1 = int(input("enter the marks in science"))
sub2 = int(input("enter the marks in maths"))
sub3 = int(input("enter the marks in social"))
sub4 = int(input("enter the marks in nepali"))
total_marks = sub4 + sub3 + sub2 + sub1
percentage = (total_marks/4)
print(f"total marks is {total_marks}")
print(f"total percentage is {percentage} %")
if percentage < 40:
    print("fail")
elif percentage >= 40 and percentage < 50:
    print("pass")
elif percentage >=50 and percentage <60:
    print("third grade")
elif percentage >= 60 and percentage<70:
    print("second grade")
elif percentage >=70 and percentage<80:
    print("first grade")
else:
    print("Distinction")

