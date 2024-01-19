'Write a program to check if a number is even or odd.'

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def even_odd(input):
    return print(["even" if number%2 == 0 else "odd" for number in input])


if __name__ == "__main__":
    user_input = [float(item) for item in list(input("Please enter your numbers here (comma-seperated): ").split(","))]
    result = even_odd(user_input)