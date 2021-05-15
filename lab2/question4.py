#given the three integers, print the smallest one.(three integers should be user input)
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))
if a<b and a<c:
    print(f"smallest number is {a}")
elif b<a and b<c:
    print(f'smallest number is {b}')
elif c<a and c<b:
    print(f"smallest number is {c}")