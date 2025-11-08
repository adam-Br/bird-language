import random
normal = input("Enter a sentence: ")
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"
def translate_to_bird (sentence):
    bird = ""
    for letter in sentence:
        if letter in vowels:
            bird += letter*3
        elif letter in consonants:
            bird += letter + random.choice(vowels)
        else:
            bird += letter
    return bird

print(translate_to_bird(normal))