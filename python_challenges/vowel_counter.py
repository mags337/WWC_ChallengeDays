'Write a function to count the number of vowels in a given string '

test_sentence = 'and what about now, how many vowels are written in this string'


def get_user_input():
    return str.lower(input('Enter a sentence: '))
    # except ValueError:
    #     print ('----Invalid input----')
    #     return None


def count_vowels(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    v = []

    for letter in sentence:
        for vowel in vowels:
            if vowel in letter:
                v.append(vowel)
    
    return ({vowels:v.count(vowels) for vowels in v})


if __name__ == '__main__':
    user_sentence = get_user_input()
    result = list(count_vowels(user_sentence).items())
    print(f'The count of vowels in the following sentence: {user_sentence} is: {result}')
