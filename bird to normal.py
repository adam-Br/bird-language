bird_s = input("Enter a sentence: ")
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"
def translate_to_normal(sentence):
    normal = ""
    counter = 0
    while counter < len(sentence):
        if sentence[counter] in vowels:
            normal += sentence[counter]
            counter +=3
        elif sentence[counter] in consonants:
            normal += sentence[counter]
            counter +=2
        else:
            normal += sentence[counter]
            counter +=1
    return normal

print(translate_to_normal(bird_s))