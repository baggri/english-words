import os

with open("words.txt","r") as words:
    string_of_words = words.read()

if os.path.exists("working_words.txt"):
    os.remove("working_words.txt")

good_letters = ['a','b','c','d','e','f','g','i','m','o','r','s','t','z']
bad_letters = ['h','j','k','l','n','p','q','u','v','w','x','y']

working_words_file = open("working_words.txt", "w")

longest_word = ''

string_of_words = string_of_words.lower()

array_of_words = string_of_words.split()

def check_word(specific_word):
    for letter in bad_letters:
        if letter in specific_word:
            break
        else:
            continue
        
    if letter =='y':
        return True

for word in array_of_words:
    if check_word(word) == True:
        working_words_file.write(word + "\n")

        if len(word) >= len(longest_word):
            longest_word = word
            print (longest_word)

    else:
        continue

print(longest_word)