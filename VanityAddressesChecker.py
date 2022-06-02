import os

with open("words.txt","r") as words:
    string_of_words = words.read()

if os.path.exists("working_words.txt"):
    os.remove("working_words.txt")

if os.path.exists("working_leet_words.txt"):
    os.remove("working_leet_words.txt")

good_letters = ['a','b','c','d','e','f','g','i','m','o','r','s','t','z'] #doesnt have functionality just so its easier to understand
letters_to_leet = {'a':'a', 'b':'b', 'c': 'c', 'd':'d', 'e':'e', 'f':'f', 'g':'9', 'i':'1', 'm':'44', 'o':'0', 'r':'2', 's':'5', 't':'7', 'z':'2'}
bad_letters = ['h','j','k','l','n','p','q','u','v','w','x','y']

working_words_file = open("working_words.txt", "w")
working_leet_words_file = open("working_leet_words.txt", "w")

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


def convert_word_to_leet(word):
    new_word = word
    for letters in word:
        for letters in good_letters:
            new_word = new_word.replace(letters, letters_to_leet[letters]) 
    return new_word


for word in array_of_words:
    if check_word(word) == True:
        working_words_file.write(word + "\n")
        working_leet_words_file.write(convert_word_to_leet(word) + "\n")

        if len(word) >= len(longest_word):
            longest_word = word

    else:
        continue


print(longest_word)
print(convert_word_to_leet(longest_word))