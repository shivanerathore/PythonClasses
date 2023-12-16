# Shivane Rathore

sentence = input("Enter a sentence with no spaces but the first letter of each word should be capitalized: ")

new_sentence = sentence[0]

for letter in sentence[1:]:
    if letter.isupper():
        new_sentence += " " + letter.lower()
    else:
        new_sentence += letter

print(new_sentence)
