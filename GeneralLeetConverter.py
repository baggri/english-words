letters_to_leet = {
    'a':'4', 
    'b':'8', 
    'c': '¢', 
    'd':'Ð', 
    'e':'3', 
    'f':'|=', 
    'g':'9',
    'h':'#',
    'i':'1', 
    'j':'_|', 
    'k':'|<', 
    'l':'|_', 
    'm':'/\/\\', 
    'n':'|\|', 
    'o':'0', 
    'p':'|°', 
    'q':'0_', 
    'r':'|2', 
    's':'5', 
    't':'7', 
    'u':'|_|', 
    'v':'\/', 
    'w':'\/\/', 
    'x':'><', 
    'y':'¥', 
    'z':'2'
    }

def convert_word_to_leet(word):
    new_word = word

    for letters in word:
        for letters in letters_to_leet:
            new_word = new_word.replace(letters, letters_to_leet[letters]) 

    print(word)
    print(new_word)


x = input('what would you like to convert: ')
convert_word_to_leet(x)