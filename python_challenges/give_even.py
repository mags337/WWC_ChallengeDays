'Write a function that takes a list of numbers and returns a new list containing only the even numbers.'

def only_even(numbers):
    return [n for n in numbers if n%2 == 0]

#example
num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(only_even(num))