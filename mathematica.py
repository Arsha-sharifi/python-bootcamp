numbers=[]
try :
    num=int(input('How many numbers?: '))
    n=1
    while n <= num :
        try :
            x=int(input(f'Enter number {n}: '))
            numbers.append(x)
            n+=1
        except ValueError :
            print('Enter number azizam')
    t=len(numbers)
    print(f'Sum = {sum(numbers)} | Average = {sum(numbers)/t} | Max = {max(numbers)} | Min = {min(numbers)}')
except ValueError :
    print('Enter number azizam')
  