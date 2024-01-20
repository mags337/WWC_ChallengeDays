'Write a program to remove duplicates from a list.'

def rm_duplicates(user_input):
    '''
    Removes duplicates from a list 
    - Parameters: A list of strings or numbers
    - Returns: A list of unique items as strings from the original list
    '''
    return list(set(user_input))

if __name__ == '__main__':
    try: 
        user_input = list(input("Please enter a list of items: ").split(","))
        result = rm_duplicates([float(item) if item.isnumeric() else item for item in user_input])
        print(f'The list without duplicates: {result}')
    except ValueError:
        print("Please enter either numbers or strings")
