# print name and age.
name = str(input('enter your name'))
age = int(input('enter your age'))
print('my name is', name, 'and my age is', age)
print('my name is ' + name + ' and my age is ' + str(age) + ' years old')
print('my name is {} and my age is {} years old'.format(name,age))
print(f'my name is {name} and my age is {age}')
print('my name is %s and my age is %d years old' % (name, age))