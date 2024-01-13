'Create a program that swaps the values of two variables.'

def swap_values(x, y):
    x, y = y, x
    return x, y

if __name__ == '__main__':
    'Get user input'
    x = input("Input one: ")
    y = input("Input two: ")

    'Call the swap_values function and store results'
    result = swap_values(x, y)

    'print the results'
    print(f'Original values: x = {x}, y = {y}')
    print(f'Swapped values: x = {result[0]}, y = {result[1]}')