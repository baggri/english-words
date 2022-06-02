good_letters = ['a','b','c','d','e','f','g','i','m','o','r','s','t','z']
letters_to_leet = {'a':'a', 'b':'b', 'c': 'c', 'd':'d', 'e':'e', 'f':'f', 'g':'9', 'i':'1', 'm':'44', 'o':'0', 'r':'2', 's':'5', 't':'7', 'z':'2'}
bad_letters = ['h','j','k','l','n','p','q','u','v','w','x','y']

def check_word(specific_word):
    for letter in bad_letters:
        if letter in specific_word:
            break
        else:
            continue
        
    if letter =='y':
        return True

def convert_word_to_leet(word):
    check_word(word)
    new_word = word

    for letters in word:
        for letters in good_letters:
            new_word = new_word.replace(letters, letters_to_leet[letters]) 
            
    print(word)
    print(new_word)


x = input('what would you like to convert:')
convert_word_to_leet(x)