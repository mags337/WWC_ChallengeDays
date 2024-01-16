'Write a program to count the occurrences of a specific character in a string.'

def count_letter(letter, sentence):
    '''
    Count the occurrences of a specific character in a string
    Parameters: 
    - letter (str): The letter to count
    - sentence (str): The sentence in which to count the occurrences
    
    Returns:
    - int: The number of occurrences
    '''
    return sentence.count(letter)

if __name__ == '__main__':
    user_input1, user_input2 = input("Enter the letter you want to count: ").lower(), input("Enter a sentence: ").lower()
    result = count_letter(user_input1, user_input2)
    print (f'The letter {user_input1} appears {result} times in  {user_input2}')

