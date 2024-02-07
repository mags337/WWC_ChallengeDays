'Write a program to remove vowels from a given string.'

def rm_vowels(text):
    vowels = set('aeiou')  
    return ''.join([letter for letter in text if letter not in vowels])

# Example
text = "Remove all vowels from this string"
print(rm_vowels(text))
