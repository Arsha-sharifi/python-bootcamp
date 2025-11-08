from datetime import datetime
with open('diary.txt','a')as file:
    while True :
        note=input('Enter your note: ').rstrip()
        if not note :
            continue
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write(f"[{now}] {note}\n")
        break
while True:
    x=input('Do you want to read previous notes?: (y/n)\n').lower()
    if x == 'n':
        print('Note saved successfully')
        break
    elif x == 'y':
        for line in open("diary.txt", "r"):
            print(line.strip())
            break
    else:
        print("Invalid Input, Try 'y' or 'n'!")
            