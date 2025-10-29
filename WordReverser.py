sntnce=input("Enter anything: ").lower()
words=sntnce.split()
reversed_words=[word[::-1] for word in words]
result=' '.join(reversed_words)
print(result)