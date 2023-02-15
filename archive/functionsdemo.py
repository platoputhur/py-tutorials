def capitalize_vowels(sentence):
    new_sentence = ""
    vowels = "aeiou"
    for ch in sentence:
        if ch in vowels:
            ch = ch.upper()
        new_sentence += ch
    return new_sentence

def print_abc():
    print("abc")
