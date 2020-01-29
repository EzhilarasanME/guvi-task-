print('R for rock\nP for paper\nS for scissor\nFirst player to score 5 points wins.')

p1=0
p2=0

while p1<5 or p2<5:
    
    x = input('Player 1 chooses: ')
    y = input('Player 2 chooses: ')
    
    if x==y:
        print('Draw')
    
    elif (x=='r' or x=='R') and (y=='p' or y=='P'):
        p2 = p2 + 1
        
    elif (x=='r' or x=='R') and (y=='s' or y=='S'):
        p1 = p1 + 1
        
    elif (x=='p' or x=='P') and (y=='r' or y=='R'):
        p1 = p1 + 1
        
    elif (x=='p' or x=='P') and (y=='s' or y=='S'):
        p2 = p2 + 1
        
    elif (x=='s' or x=='S') and (y=='p' or y=='P'):
        p1 = p1 + 1
        
    elif (x=='s' or x=='S') and (y=='r' or y=='R'):
        p2 = p2 + 1
        
    else:
        print('Either of the player chose invalid choice')
        
if p1 == 5:
    print('Player 1 wins')
else:
    print('Player 2 wins')
