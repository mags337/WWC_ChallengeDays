'Write a program to reverse a given string.'

def reverse_string(string):
    try:
        rev = [string[-i-1] for i,letter in enumerate(string)]
        return ''.join(map(str, rev))
    except ValueError:
        return "ValueError: must be a string"
    

if __name__ == "__main__":
    user_input = input("Ener the string you want to reverse: ")
    result = reverse_string(user_input)
    print( f'The srting {user_input} has been reversed successfully: {result}')
