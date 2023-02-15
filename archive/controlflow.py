vowels = "aeiou"
sentence = "lazy fox jumped over the fence"

new_sentence = ""
# for ch in sentence:
#     if ch in vowels:
#         ch = ch.upper()
#     new_sentence += ch
sentence_len = len(sentence)
i = 0
while True:
    ch = sentence[i]
    if ch in vowels:
        ch = ch.upper()
    new_sentence += ch
    i += 1
    if i >= sentence_len:
        break

print(new_sentence)
