def get_number():
    while True :
        try :
            return float(input('Enter a number: '))   
        except ValueError :
             print('Invalid Input')
             
def get_operator():
    while True:
        op=input('Enter operator (+, -, *, / OR q for quit): ').strip() 
        if op in ['+','-','*','/','q'] :
            return op
        print('Invalid  Input')

def calculate(a, b, op) :
    if op == '+' : return a+b
    elif op == '-' : return a-b 
    elif op == '*' : return a * b 
    elif op == '/' : 
        return 'Cannot divide by zero' if b==0 else a/b
    
def main() :
    result=get_number()
    while True :
        op=get_operator()
        if op == 'q' :
            print('Bye Bye!')
            break 
        num=get_number()
        result=calculate(result,num,op)
        print(f'Result: {result}\n')
        
main()