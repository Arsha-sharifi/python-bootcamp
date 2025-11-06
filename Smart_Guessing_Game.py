def main():
    print("Think of a number an I'll guess")
    t=1
    while True :   
        try :
            high=int(input("Enter the upper limit: "))
            break
        except ValueError : 
            print('Enter a number!') 
            continue
    low=1
    guess=(low+high)//2
    print(f'my guess is {guess}')
    while True : 
        x = input("Enter ('higher', 'lower', or 'correct'): ").lower()
        if x == 'higher':
            low=guess+1
            t+=1
        elif x == 'lower':
            high=guess-1
            t+=1
        elif x == 'correct' :
            print(f'YAY!\nI guessed correct in {t} times :)')
            break
        else:
            print(f'Invalid Input, Try again')
            continue
        if low > high:
            print("Hmm... something's off. You might've given WRONG hints")
            break
        guess=(low+high)//2
        print(f'my guess is {guess}')
        
main()
            
        
