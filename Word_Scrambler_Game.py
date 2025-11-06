import random
def get_random_word():
    words= ["python", "computer", "program", "keyboard", "mouse", "screen", "monitor", "internet", "website", "browser",
    "code", "function", "variable", "class", "object", "string", "integer", "float", "boolean", "list",
    "dictionary", "tuple", "array", "loop", "while", "for", "if", "else", "elif", "print",
    "input", "output", "file", "open", "close", "read", "write", "append", "import", "module",
    "package", "error", "debug", "compile", "execute", "process", "memory", "storage", "data", "database",
    "server", "client", "network", "socket", "request", "response", "json", "html", "css", "javascript",
    "framework", "library", "algorithm", "logic", "syntax", "command", "terminal", "shell", "editor", "text",
    "folder", "directory", "path", "system", "update", "install", "remove", "save", "load", "run",
    "test", "result", "value", "return", "define", "classify", "connect", "disconnect", "search", "replace",
    "language", "keyboard", "monitor", "country", "explain", "project", "practice", "example", "science", "technology"]
    word=random.choice(words)
    return word
    
def scramble_word(word):
    letters=list(word)
    random.shuffle(letters)
    scrambled=''.join(letters)
    print(f"Scrambled word: {scrambled}")
    max_tries=3
    tries=0
    while tries < max_tries :
        guess = input("Enter your guess: ").strip().lower()
        if guess == word:
            print("Nice! Correct guess!")
            return True
        else:
            tries += 1
            if tries == max_tries:
                print(f"You failed! The word was '{word}'.")
                return False
            print("Wrong! Try again.")
        

def play_round():
    score = 0
    while True:
        print("\n--- New Round ---")
        word = get_random_word()
        result = scramble_word(word)
        if result == True:
            score += 1
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == 'n':
            print(f"\nYour final score is {score}")
            break
    
play_round()
    