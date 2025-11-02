def recursive_factorial(n, depth=0):
    indent = "  " * depth
    if n < 0:
        print(f'{indent}Factorial not defined for negative numbers')
        return None
    print(f'{indent}Entering recursive_factorial({n})')
    if n == 1:
        print(f'{indent}Base Case reached, returning 1')
        return 1 
    result = n * recursive_factorial(n-1,depth+1)
    print(f'{indent}Returning {n} * recursive_factorial({n-1}) = {result}')
    return result
while True:
    try:
        num=int(input('Enter a number: '))
        print(f'\nFinal result: {recursive_factorial(num)}')
    except ValueError :
        print('Invalid Input')
