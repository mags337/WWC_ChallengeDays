'Write a program to print the multiplication table of a given number.'


def get_multiply_table(input_number, table_nr):
    """
    Generates the multiplication table for a given number up to a specified range.

    Parameters:
    - input_number (int): The number for which the multiplication table is to be generated.
    - table_nr (str): The range end number for the multiplication table.

    Returns:
    - list: A list containing the multiplication table for the input_number within the specified range.

    Example:
    >>> get_multiply_table(5, '10')
    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    
    Note:
    - The input_number should be an integer, and table_nr should be a string representing an integer.
    - If the user provides an invalid input, a ValueError will be raised.

    """
    table = range(1,int(table_nr)+1)
    return [num*input_number for num in table]


if __name__ == '__main__':
    try:
        user_input, table_nr = int(input("Enter the number you want the multiplication table for: ")), input("Range end nr. for multiplication table: ")
        result = get_multiply_table(user_input, table_nr)
        print(f'The multiplication table for {user_input} is {result}')
    except ValueError:
        None