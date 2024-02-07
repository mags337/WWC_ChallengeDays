'Create a program to remove a specific element from a set.'

def rm_from_set(rm, my_set):
    my_set.discard(rm)
    return None


my_set = {1, 2, 3, 4}
print(my_set)
rm_from_set(3, my_set)
print(my_set)