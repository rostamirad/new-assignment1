import math

print('Welcome to my calculator! 🤗')

while True:
    print('menu:')
    print('+: sum')
    print('-: sub')
    print('*: mul')
    print('/: div')
    print('log')
    print('sin')
    print('cos')
    print('tan')
    print('cot')
    print('sqrt')
    print('factorial')
    print('Please enter zero for exit:) ❌')

    op = input("Please enter the operation that you want!: ")

    if op != 'zero':

        if op == '+' or op == '-' or op == '*' or op == '/':
            a = float(input('Please enter the first number: '))
            b = float(input('Please enter the second number: '))
        elif op == 'log' or op == 'sin' or op == 'cos' or op == 'tan' or op == 'cot' or op == 'sqrt' or op == 'factorial':
            a = float(input('Please enter the number: '))
        else:
            print('Please select your operation from the options in our menu 😉')
            continue

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                result = 'Can not divided by zero! ❌'
            else:
                result = a / b
        elif op == 'log':
            result = math.log(a)
        elif op == 'sin' or op == 'cos' or op == 'tan' or op == 'cot':
            c = math.radians(a)
            if op == 'sin':
                result = math.sin(c)
            elif op == 'cos':
                result = math.cos(c)
            elif op == 'tan':
                result = math.tan(c)
            else:
                result = math.cot(c)
        elif op == 'sqrt':
            result = math.sqrt(a)
        elif op == 'factorial':
            result = math.factorial(a)
        
        print('answer: ', result)
        continue
    
    
    if op == 'zero':
        print('Thank you!😘')
        break