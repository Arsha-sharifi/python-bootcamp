words=input('Enter Anything: ').lower()
list_word=words.split()
dict_word={}

for word in list_word :
    dict_word[word]=dict_word.get(word,0)+1
    
max_word = max(dict_word, key=dict_word.get)
print(f"The most frequent word is: '{max_word}' with {dict_word[max_word]} occurrences.")
