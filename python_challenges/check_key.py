'Day 23: Write a program that checks if a key exists in a dictionary.'

def search_key(search_dict, search_input):
        if search_input in search_dict.keys():
            print(f'The key "{search_input}" was found in the dictionary')
        else:    
            print(f'The key "{search_input}" was NOT found in the dictionary')

example_dict = {"apple":3, "orange":7, "kiwi":8}
example_input1 = "orange"
example_input2 = "banana"

search_key(example_dict, example_input1)
# Output: The key "orange" was found in the dictionary

search_key(example_dict, example_input2)
# Output: The key "banana" was NOT found in the dictionary