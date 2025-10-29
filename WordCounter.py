fhand=open(input('Enter a file:'))
dict_words={}
for line in fhand :
    line=line.rstrip().lower()
    words=line.split()
    for word in words :
        dict_words[word]=dict_words.get(word,0)+1

sorted_list = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
print(sorted_list[:5])
