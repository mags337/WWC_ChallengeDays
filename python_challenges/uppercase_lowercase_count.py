'Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it'

def get_upper_lower_lettercount(user_input):
    from string import ascii_letters

    upper = [letter for letter in user_input if letter in set(ascii_letters.upper())]
    lower = [letter for letter in user_input if letter in set(ascii_letters.lower())]
    return print(f'There are {len(lower)} lowercase and {len(upper)} uppercase letters in the given string')

# test = "Dive into daily Python challenges. UPPER and lowercase"
# get_upper_lower_lettercount(test)

if __name__ == '__main__':
    user_input = input("Please enter your sentence: ")
    result = get_upper_lower_lettercount(user_input)