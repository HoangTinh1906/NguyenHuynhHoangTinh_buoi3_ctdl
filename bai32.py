sentence='My name Elshad'
def is_consonant(letter):
    vowels="aeiou"
    return letter.isalpha() and letter.lower() not in vowels
consonant=[i for i in sentence if is_consonant(i)]
print(consonant)