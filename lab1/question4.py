#given the integer N-the number of minutes that is passed since midnihght - how many hours and minutes are displayed on the 24 digital clock? the program should print two numbers: the number of hours (between 0 and 23) and the number of minutes(between 0 and 59). for example, if N=150 then 150 minutes have passed since midnight- i.e now is 2:30am . so, the program should print 2:30
num = int(input('enter a number'))
hour = num//60
minutes = num % 60
print(f'the time now is {hour} : {minutes}')
