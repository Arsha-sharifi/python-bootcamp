num=input('Enter an number: ')
cleaned_num=num.replace('-','').replace('.','')
if cleaned_num.isdigit() :
    print(f'the number has {len(cleaned_num)} digits')
else :
    print('Enter number palasht')
