print('Triangle drawing possibility program! ')

while True:
    d = int(input('Please enter 1 for continue and 0 for exit: '))  

    if d == 1:
            
        a = float(input('Please enter the first dimension: '))
        b = float(input('Please enter the second dimension: '))
        c= float(input('Please enter the third dimension: '))

        if a == 0 or b == 0 or c == 0:
            print('This triangle can not be drawn! ❌')
            continue

        elif a < b + c and     b < a + c and    c < a + b:
            print('This triangle can be drawn! ✅')
            continue

        else:
            print('This triangle can not be drawn! ❌')
            print('note: The size of each side of the triangle must be smaller than the sum of the other two sides!! ❗❗')
            print('Please try again:) 😉')
            continue

    elif d == 0:
        print('Thank you!😘')
        break