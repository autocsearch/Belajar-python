# 🧠 Challenge: Capitalize First Letter of Each Word
# Input:
# sentence = "hello from hennge"
# Expected output:
# "Hello From Hennge"
# Try it using what you know so far (split(), loops, f-strings), or ask me to walk through it with you!


def capitalize_sentence(sentence):
    words = sentence.split(" ")
    capitalized = []

    for word in words:
        capitalized_word = word.capitalize()
        capitalized.append(capitalized_word)

    return " ".join(capitalized)

# Try it:
sentence = "hello from hennge"
print(capitalize_sentence(sentence))


