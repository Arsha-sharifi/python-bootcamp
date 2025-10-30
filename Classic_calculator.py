print("Welcome to Calculator\n------------------------------")
while True :
    try :
        if not 'result' in locals() :
            result = float(input('Enter first number: '))
        op=input('Enter operator (+, -, *, / or q to quit): ').strip()
        if op == 'q' :
            print('Bye Bye')
            del result
            break
        if op == '':
            print('No operator entered, Wanna do smth?!')
            continue 
        num=float(input('Enter next number: ')) 
        if   op == '+' :
            result+=num
        elif op == '-' :
            result-=num
        elif op == '*' :
            result*=num
        elif op == '/' :
            if num == 0:
                print("Division by zero not allowed!")
                continue
            result/=num
        else :
            print('Invalid Input')
        print(f"\nThe result is: {result}\n-------------------------")
            
    except ValueError :
        print('Enter a valid number baka')
