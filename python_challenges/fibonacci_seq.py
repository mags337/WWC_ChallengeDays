'Write a program to print the first n numbers of a Fibonacci sequence'

def fib(n):
    """
    Generate the first n numbers of the Fibonacci sequence.

    Parameters:
    - n (int): The number of Fibonacci numbers to generate.

    Returns:
    - list: A list containing the first n Fibonacci numbers.
    """
    fib_nr = [0,1]
    while len(fib_nr) < n:
        fib_nr.append(fib_nr[-1]+fib_nr[-2])
    return fib_nr[:n]

if __name__ == '__main__':
    user_input = int(input('Enter how many numbers of Fibonacci sequences you want: '))
    print("user", user_input)
    result = fib(user_input)
    print("numbers", result)
    print(f'The first {user_input} numbers of the Fibonacci sequences are: {result}')