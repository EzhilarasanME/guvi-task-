import random

a = ['dad', 'mom', 'bat', 'car', 'bus', 'pen', 'dog', 'cat']
points = 0
b = random.choice(a)

for i in range(5):
    c = input('Enter a character: ')
    if c in b:
        print('Good')
        points = points + 1
        if points == 3:
            break
    else:
        print('You entered a wrong character')
        
if points == 3:
    print('Won')
    print (b)
else:
    print('Lost')
