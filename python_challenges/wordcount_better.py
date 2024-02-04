'Write a function that counts the frequency of each word in a sentence'

# Libraries needed
import re
from collections import Counter


sen = "How often does this word come up in this sentence and how about this and that?"
def count_words(sentence):
    '''
    Count the frequency of each word in a sentence.

    Parameters:
    sentence (str): The input sentence to count word frequency from.

    Returns:
    Counter: A Counter object containing the frequency of each word in the sentence.
    '''
    words = re.findall(r'\b\w+\b', sen.lower())
    return Counter(words)


if __name__ == '__main__':
    user_input = input('Enter a string to count word frequency: ')
    result = count_words(user_input)
    print(f'{result}')