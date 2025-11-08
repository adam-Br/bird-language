import random
sentence = input("Enter a sentence: ")
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"
bird = ""
for letter in sentence:
    if letter in vowels:
        bird += letter*3
    elif letter in consonants:
        bird += letter + random.choice(vowels)
    else:
        bird += letter

print(bird)