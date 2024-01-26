'Write a program to find the sum of all elements in a list.'

def sum_of_elements(input_list):

    '''
    Calculate the sum of a list of numbers.

    Parameters:
    - numbers (list of int or float): A list of numeric values.

    Returns:
    float: The sum of the input numbers.
    '''
    
    try:
        'Filtering the non-numerical elements in the given list'
        input = [element for element in input_list if isinstance(element, (int,float))]
        return sum(input)
    except ValueError:
        return "ValueError"

if __name__ == '__main__':      
    try: 
        'Get the user input and convert it to a list of floats, then calculate and save the sum of the list elements'
        user_input = [float(item) for item in list(input("Please enter your list of elements here (comma-separated): ").split(","))]
        result = sum_of_elements(user_input)
        print(f' The sum of the list {user_input} is: {result}')
    
    except ValueError:
        print("----ValueError. Input elements must be int or float types!----")
