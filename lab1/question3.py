# N students take K apples and distribute them among each other evenly. the remaining (unvisible) part remains in the basket. how many apples will remain in the basket? the program reads the the number N and K. it should print the two answers fpr the question above.
students = int(input('enter the number of students'))
apples = int(input('enter the number of aples'))
D = (apples//students)
R = (apples % students)
print(f'each students get {D} apples')
print(f'the remaining apples {R}')
