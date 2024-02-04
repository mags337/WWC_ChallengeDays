'Create a program that capitalizes the first letter of each word in a sentence'
# Library needed
import re

def capitalize_words(sentence):
    '''
    Capitalize the first letter of each word in a sentence.

    Parameters:
    sentence (str): The input sentence to capitalize words from.

    Returns:
    str: A new sentence with the first letter of each word capitalized.
    '''
    capital_words = [word.capitalize() for word in re.findall(r'\b\w+\b', sentence.lower())]
    return " ".join(capital_words)

if __name__ == '__main__':
    user_input = input('Write sentence to capitalize: ')
    result = capitalize_words(user_input)
    print(f'{result}')