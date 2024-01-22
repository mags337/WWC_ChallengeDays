'Write a program to reverse a given string.'

def reverse_string(string):
    '''
    Reverses the order of characters in a given string.

    Parameters:
    - string (str): The input string to be reversed.
    Returns:
    - str: The reversed string.
    Raises:
    - ValueError: If the input is not a string.
    '''
    try:
        # Use list comprehension to create a reversed version of the string
        # by iterating over its characters in reverse order.
        rev = [string[-i-1] for i,letter in enumerate(string)]
        # Join the reversed characters into a new string.
        return ''.join(map(str, rev))
    except ValueError:
        # Handle the case where the input is not a string.
        return "ValueError: must be a string"
    

if __name__ == "__main__":
    user_input = input("Ener the string you want to reverse: ")
    result = reverse_string(user_input)
    print( f'The srting {user_input} has been reversed successfully: {result}')
