# Pig Latin - Pig Latin is a game of alterations played on the English language 
# game. To create the Pig Latin form of an English word the initial consonant 
# sound is transposed to the end of the word and an ay is affixed (Ex.: "banana"
# would yield anana-bay). Read Wikipedia for more information on rules.

def transpose_word(word):
    vowels = ["a", "e", "i", "o", "u"]

    # word begins with vowel
    if word[0] in vowels:
        return word + "way"

    # word begins with consonant -> find first vowel
    for character in word:
        if character in vowels:
            split_index = word.find(character)
            return word[split_index:] + word[:split_index] + "ay"
        
    # word only consists of consonants
    return word + "ay"

# We are handling full capitalisation and first letter capitalisation.
# Everything else is converted to lowercase.
def handle_capitalization(word):
    if word.isupper():
        return transpose_word(word.lower()).upper()
    elif word[0].isupper():
        return transpose_word(word.lower()).capitalize()
    else:
        return transpose_word(word.lower())

def split_text(text):
    piglatin_text = ""
    for sentence in text.split("."):
        for phrase in sentence.split(","):
            for word in phrase.split():
                piglatin_text += " " + handle_capitalization(word)
            piglatin_text += ","

        # Removes trailing punctuation
        piglatin_text = piglatin_text[:-1]

        piglatin_text += "."
    
    # Removes trailing punctuation
    piglatin_text = piglatin_text[:-1]
    
    return piglatin_text.strip()

def print_in_piglatin(text):
    print(split_text(text))

string = ("This is an example of Pig Latin. As you can see, it is silly," + 
          "but sort of fun for children.")

print(string)
print_in_piglatin(string)