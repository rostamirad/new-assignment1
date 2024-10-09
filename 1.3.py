print('Welcome 🤗')

while True:
    a = int(input('Please enter 1 for continue and 0 for exit: '))

    if a == 1:
        print('Student profile: 👤')
        b = input('Please enter the first name: ')
        c = input('Please enter the surname: ')

        print('student grades: 🔢')
        d = float(input('First grade:'))
        e = float(input('Second grade:'))
        f = float(input('Third grade:'))

        average =  (d + e + f)/3

        if average >= 17:
            print('student: ', b , c)
            print('average: ' , average , ':' , 'Great! 🟢')
            continue

        elif 17 > average >= 12:
            print('student: ', b , c)
            print('average: ' , average , ':' , 'Normal 🟡')
            continue
        
        elif average < 12:
            print('student: ', b , c)
            print('average: ' , average , ':' , 'Fail! 🔴')
            continue
    
    if a == 0:
        print('Thank you! 😘')
        break