def print_upper_words(words,letter_dict):
    
    for word in words:
        for letter in letter_dict:
            if word[0] == letter:
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],{'h','y'})
 