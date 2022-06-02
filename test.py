array_of_words = ['hey', 'test']
bad_letters = ['h', 'g']

def check_word(specific_word):
    for letter in bad_letters:
        if letter in specific_word:
            break
        else:
            return specific_word

print(check_word('bb'))

""" for word in array_of_words:
    if check_word(word) == True:
        print(word) """