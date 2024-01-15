' Write a program to find the maximum and minimum values in a list.'


def get_min_max(input_list):
    '''Find the maximum and minimum values in a list
    Parameters: 
    - Input_list (int/float): a list of numeric values
    Returns:
    - A string about the maximum and minimum values
    - If the list is empty, the function returns: "The list is empty"
    '''

    return f'The maximum value of the list is {max(input_list)}, and the minimum value is {min(input_list)}'

if __name__ == '__main__':
    try:
        user_input = [float(item) for item in input("Please enter your list of elements here (comma-seperated): ").split(",")]
        print(get_min_max(user_input))
    except ValueError:
        print("The list is empty")