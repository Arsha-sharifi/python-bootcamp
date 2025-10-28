try: 
    num=int(input('When did you born?: '))
    age=2025-num
    if age <= 0 :
        print('u think youre funny ?')
    else:  
        print(f'you are {age} years old')
        if age >= 60 :
            print('Daaammnn youre old')
        elif age >= 30 :
            print(f'Hows life?\nyoull be 60 in {60-age} years :)')
        else :
            print(f'Way to go buddy, youll be 30 in {30-age} years ')
except ValueError :
    print('INVALID INPUT baka')
