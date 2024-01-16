'Write a program to check if a number is positive, negative, or zero.'

def value_check(test):
        '''
        This function takes a list of numbers as input and returns a list of strings
        indicating whether each number is positive, negative, or null (zero).

        Parameters:
        - test (list): A list of numbers to be checked.

        Returns:
        - list: A list of strings, each indicating the nature of the corresponding number
        (e.g., "5 is positive", "-3 is negative", "0 is null").
        '''
        return ([f"{num} {'is positive' if num > 0 else 'is negative' if num < 0 else 'is null'}" for num in test])
    
if __name__ == '__main__':
    try:
        user_input = [float(item) for item in list(input("Please enter your numbers here (comma-seperated): ").split(","))]
        result = value_check(user_input)
        print(result)
    except ValueError:
        print("ValueError: Please enter a number")

