import math

print('Welcome 🤗')

while True:
    a = int(input('Please enter 1 for continue and 0 for exit: '))

    if a == 1:
        weight = float(input('Please enter the weight in kg: '))
        height = float(input('Please enter the height in meter: '))

        BMI = weight/math.pow(height, 2)

        if BMI <= 18.5:
            print('Your BMI index is: ', BMI)
            print('Underweight! 💙')
            continue
        
        elif 18.5 < BMI <= 24.9:
            print('Your BMI index is: ', BMI)
            print('Normal weight:) 💚')
            continue

        elif 25 <= BMI <= 29.9:
            print('Your BMI index is: ', BMI)
            print('Overweight! 💛')
            continue

        elif 30 <= BMI <= 34.9:
            print('Your BMI index is: ', BMI)
            print('Obesity! 🧡')
            continue
        
        elif 35 <= BMI <= 39.9:
            print('Your BMI index is: ', BMI)
            print('Over obesity!! 💔')
            continue
    
    if a == 0:
        print('Thank you 😘')
        break