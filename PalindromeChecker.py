wrd=input('Enter a word: ').lower()
reversed_word=wrd[::-1]
if wrd.isalpha() :
    if wrd == reversed_word :
        print(f'The word is a Palindorme!')
    else :
        print(f'The word is not a Palindorme!')
else: 
    print('Enter a word baka')