import random
num=random.randint(1,100)
t=1
max_tries=10
while True :
    try :
        if t==1 :
            x=int(input('Guess the number: '))
            
        else :
            x=int(input('Guess again: '))
            
        if x==num : 
            if t==1 :
                print('HOLY MOLY,you guessed in the first try!')
                break
            
            else:
                print(f'Correct! You guessed it in {t} tries.')
                break   
               
        elif x > num+10 :
            print('Too high\n')
            
        elif x < num-10 :
            print('Too low\n')
            
        elif num-2 <= x <= num+2 :
            print('Super close\n')
            
        else :
            print('Close guess!\n')
            
        if t > max_tries : 
            print('You lost,Guess better next time <3')
            break
        
        t+=1
        
    except ValueError :
        print('Invalid input, Enter a number!')