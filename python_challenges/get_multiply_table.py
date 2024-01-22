'Write a program to print the multiplication table of a given number.'


def get_multiply_table(input_number, table_nr):
    table = range(1,int(table_nr)+1)
    return [num*input_number for num in table]


if __name__ == '__main__':
    try:
        user_input, table_nr = int(input("Enter the number you want the multiplication table for: ")), input("Range end nr. for multiplication table: ")
        result = get_multiply_table(user_input, table_nr)
        print(f'The multiplication table for {user_input} is {result}')
    except ValueError:
        None