#for given integer x, print "true" if it is positive, print "false" if it is negative and print "zero" if it is 0.
a = int(input('enter a number'))
if a < 0:
    print("false")
elif a == 0:
    print("zero")
else:
    print("true")