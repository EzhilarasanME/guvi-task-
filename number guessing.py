import random

a=['a','b','d','t','g','y']
b=random.choice(a)
for i in range(6):
     c=input('')
     if(b==c):
         print ('you win$')
     else:
         print ('try again')
         
else:
    print ('you LOST')
