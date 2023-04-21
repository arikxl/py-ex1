def add(x, y):
    answer = x + y
    print(f'{x} + {y} = {answer}' )

def sub(x, y):
    answer = x - y
    print(f'{x} - {y} = {answer}' )

def mul(x, y):
    answer = x * y
    print(f'{x} * {y} = {answer}' )

def div(x, y):
    answer = x / y
    print(f'{x} / {y} = {answer}' )

print('A. Addition')
print('B. Subtraction')
print('C. Multiplication')
print('D. Division')
print('E. Exit')

choice = input('input your choice: ')

if choice == 'a' or choice == 'A':
    print('Addition')
    x = int(input('Choose the first number: '))
    y = int(input('Choose the second number: '))
    add(x,y)
elif choice == 'b' or choice == 'B':
    print('Subtraction')
    x = int(input('Choose the first number: '))
    y = int(input('Choose the second number: '))
    sub(x, y)
elif choice == 'c' or choice == 'C':
    print('Multiplication')
    x = int(input('Choose the first number: '))
    y = int(input('Choose the second number: '))
    mul(x, y)
elif choice == 'd' or choice == 'D':
    print('Division')
    x = int(input('Choose the first number: '))
    y = int(input('Choose the second number: '))
    div(x, y)
elif choice == 'e' or choice == 'E':
    print('Have a good day!')
    quit()