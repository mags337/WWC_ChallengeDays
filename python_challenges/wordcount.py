'Write a function that counts the frequency of each word in a sentence'

sen = "How often does this word come up in this sentence and how about this and that?"

import re

def count_words(sentence):
    words = re.sub(r'[^a-zA-Z]', ' ', sen).lower().split(" ")

    word_dict = {}
    for word in words:
        word_dict[word] =  0

    for word in words:
        if word in words:
            word_dict[word] += 1

    return word_dict


print(count_words(sen))
