'Task: Write a function to count the number of vowels in a given string '

def count_vowels(sentence):
    'Create a set of vowels for faster processing'
    'Use dictionary comprehension to create a dictionary of vowel counts'
    'Iterate over each vowel in the set, check if the vowel is present in the sentence'
    'If present, create a key:value pair with the vowel and its count in the sentence'
    
    vowels = set('aeiou')   
    return {vowel: sentence.count(vowel) for vowel in vowels if vowel in sentence}

if __name__ == '__main__':
    'Get user input and convert it to lowercase for case-sensitive matching'
    'call the count_vowels function and store the result'
    'print the result'

    user_sentence = input('Enter a sentence: ').lower()
    result = count_vowels(user_sentence)
    print(f'The count of vowels in the following sentence: "{user_sentence}" is: {result}')