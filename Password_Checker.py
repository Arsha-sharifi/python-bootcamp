def get_password():
        while True :
            password=input('Enter your password: ')
            if not password :
                print('Enter your password please: ')
                continue
            return password
def check_strength(password):
    points=0
    special_chars = "!@#$%^&*()_+-="
    for x in password :
        if x in special_chars : points += 1
    if len(password) > 7 : points += 1
    if any(c.isalpha() for c in password): points += 1
    if any(c.isdigit() for c in password): points += 1
    if any(c.isupper() for c in password): points += 1

    if points >= 4 :
        print('STRONG')
    elif points > 2 :
        print('MEDIUM')
    else:
        print("WEAK")
    
def main():
    result=get_password()
    check_strength(result)
        
main()