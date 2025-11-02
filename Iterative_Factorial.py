def iterative_factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    print(f'Starting iterative_factorial({n})')
    result=1
    for i in range(1,n+1):
        print(f'Multiplying result ({result}) by {i}')
        result*=i
    print(f'Final result after loop: {result}')
    return result

while True :
    try : 
        num=int(input('Enter a number: '))
        print(f'\nFinal result: {iterative_factorial(num)}')
    except ValueError :
        print('Invalid Input')
    