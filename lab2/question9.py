# 9.Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.Hint: •a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100•a year is always a leap year if its number is exactly divisible by 400.
year = int(input("enter a year"))
if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is leap year")
elif year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")

else:

    print(f"{year} is not a LEAP year")