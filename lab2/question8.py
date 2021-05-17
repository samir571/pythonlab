# a = float(input('enter a number'))
# b = a%10 #2
# c = a//10 #22
# d = c%10 #2
# e = c//10 #2
# f = e + b + d
# print(f"the sum is {f}")

def fun(num):
    if num<0:
        return 0
    else:
        return fun(num-1)
print(fun(5))


