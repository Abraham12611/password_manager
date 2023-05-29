import random
import string

def generate_password(min_length, numbers=True, special=True):
    letters = string.ascii_letters
    digits = string.digits
    spec_char = string.punctuation
    
    character = letters
    if numbers:
        character += digits
    if special:
        character += spec_char
        
    passwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while meet_criteria or len(passwd) < min_length:
        new_char = random.choice(character)
        passwd += new_char
        
        if  new_char in digits:
            has_number  = True
        elif new_char in spec_char:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special:
            meet_criteria = meet_criteria and has_special                                    
    return passwd

