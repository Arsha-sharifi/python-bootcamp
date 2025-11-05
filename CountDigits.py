while True :
    num=input('Enter a number: ')
    if not num:
        print('Enter a numberrr!!')
        continue
    cleaned_num=num.replace('-','').replace('.','')
    if not cleaned_num.isdigit():
        print('Enter a numberrr!!')
        continue
    print(f'The number has {len(cleaned_num)} digits')
