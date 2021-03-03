#A school decided to replace the desks in three classrooms. each desk sits two students. given the number of students in each class, print the smallest possible number of desks that can be purchased. the program should read three integers: the number of students in each of the three classes, a,b and c respectively. in the first test there are three groups. the first group has 20 students and thus needs 10 desks. the second group has 21 students, so they can get by with no fewer than 11 desks, 11 desks are also enough for the third group of 22 students. so, we need 32 desks in total.
classA = int(input('enter the number of students in classA'))
classB = int(input('enter the number of students in classB'))
classC = int(input('enter the number of students in classC'))
total = classA + classB + classC
if total % 2 == 0:
    desk = total/2
    print(f'the number of desk needed {desk}')
else:
    desk = ((total + 1) // 2)
    print(f'the number of desk needed {desk}')