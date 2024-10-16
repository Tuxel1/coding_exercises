# Vigenere / Vernam / Ceasar Ciphers - Functions for encrypting and decrypting 
# data messages. Then send them to a friend.

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt_vigenere(text, cypher):
    count = 0
    text = text.upper()
    encrypted_text = ""

    for character in text:
        if character in " .,-;:_":
            encrypted_text += character
            continue

        # use correct encryption letter
        encryption_letter = cypher[count % len(cypher)]
        count += 1

        # shift letter according to encryption letter
        character = ALPHABET[(ALPHABET.find(character) 
                              + ALPHABET.find(encryption_letter)) 
                              % len(ALPHABET)]
        encrypted_text += character
    
    return encrypted_text

def decrypt_vigenere(text, cypher):
    count = 0
    text = text.upper()
    decrypted_text = ""

    for character in text:
        if character in " .,-;:_":
            decrypted_text += character
            continue

        # use correct encryption letter
        encryption_letter = cypher[count % len(cypher)]
        count += 1

        # shift letter according to encryption letter
        character = ALPHABET[(ALPHABET.find(character)
                              - ALPHABET.find(encryption_letter))
                              % len(ALPHABET)]
        decrypted_text += character
    
    return decrypted_text

user_input = "This is an example text. I can do this, so can you."
cypher_word = "CAESAR"

print(decrypt_vigenere(encrypt_vigenere(user_input, cypher_word), cypher_word))