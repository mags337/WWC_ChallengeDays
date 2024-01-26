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
        #-1: start steps from the back to the front
        return string[::-1]
    except ValueError:
        # Handle the case where the input is not a string.
        return "ValueError: must be a string"
    

if __name__ == "__main__":
    user_input = input("Enter the string you want to reverse: ")
    result = reverse_string(user_input)
    print( f'The string {user_input} has been reversed successfully: {result}')
