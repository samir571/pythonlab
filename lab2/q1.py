#Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
lst = [0,2,4,5,6,8,10]
for i in lst:
    if i == 5:
        print("5 is in the list")
        break
else:
    print("5 is not in the lsit")
