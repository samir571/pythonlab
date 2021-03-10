# write a python program to convert seconds into day, hour, minutes
second = int(input('enter the value of second'))
minutes = second/60
hour = minutes/60
days = hour/24
print(f"total minutes for given second is {minutes} minute")
print(f"total hour for given second is {hour} hour")
print(f"total day for given second is {days} day")
