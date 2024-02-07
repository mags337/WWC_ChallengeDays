'Create a program to find the second-largest element in a list.'

def find_second_largest(input_list):
    input_list.sort()
    return input_list[-2]


# Example 
l = [1, 5, 7, 9, 22, 566, 788, 22]
print(find_second_largest(l))