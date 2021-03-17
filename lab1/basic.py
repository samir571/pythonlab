# game finding a secret number within 3 attempts using while loop
num = 69
t = 0
while t<3:
    num_1 = int(input('guess a number'))
    if num_1 == num:
        print("congrats! you won")
        break
    else:
        print("wrong")
        t=t+1
else:
    print("your guess period is over you loser")



