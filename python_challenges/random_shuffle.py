'Write a program to shuffle the elements of a list randomly.'

def shuffle_input(user_input):
    '''
    Generate a random shuffle of the elements of a list (strings or numeric)
    - Parameters: user_input list of strings or numbers, separated by commas.
    - Returns: A randomly shuffled list of elements (str/float) from the input list. 
    '''
    import random
    random.shuffle(user_input)
    return user_input

if __name__ == '__main__':
    user_input = list(input('Please enter the list to be shuffled (comma-separated): ').split(','))
    # If list element is numeric, its converted to a float, while strings stay as strings
    result = shuffle_input([float(item) if item.isnumeric() else item for item in user_input])
    print(f'The list before {user_input} and after being shuffled: {result}')


