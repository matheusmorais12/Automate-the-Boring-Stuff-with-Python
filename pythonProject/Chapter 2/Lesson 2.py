# 1. Boolean Values

spam = True
spam2 = False
print(spam, spam2)

# 2. Comparison Operators

print('The first test: ', 42 == 42)
print('The second test: ', 42 == 92)
print('The third test: ', 1 != 3)
print('The fourth test: ', 2 != 5)
print('The fifth test: ', 'hello' != 'hello')
print('The sixth test: ', 100 > 42)
print('The seventh test: ', 500 < 42)
print('The eighth test: ', 42 <= 42)
print('The ninth test: ', 490 >= 42)

# 3. Booleans Operators

var = (4 < 5) and (5 < 6)
var2 = (4 < 5) and (8 < 6)
var3 = (4 == 5) or (5 != 6)
print(var, var2, var3)

# 4. If Statements

print('What is your name?  ')
x = input()
if x == 'Alice':
    print('Hi, Alice')

# 5. Else Statements

print('What is your name?  ')
x = input()
if x == 'Matheus':
    print('Hi, Matheus')
else:
    print('Hello, stranger')

# 6. Elif Statements

print('What is your name?  ')
x = input()
print('How old are you?  ')
age = int(input("Enter age:"))

if x == 'Matheus':
    print('Hi, Matheus')
elif age > 25:
    print('You are not Matheus')
elif age <= 25:
    print('You are Matheus')









