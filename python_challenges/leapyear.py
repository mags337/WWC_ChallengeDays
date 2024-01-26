'Create a program that checks if a year is a leap year.'
'''
Leap years occur mostly every 4 years, 
but every 100 years we skip a leap year
unless the year is devisable by 400
'''

def isitleap(user_input):
    for year in user_input:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(year, "LEAP YEAR!")
        else:
            print(year, "NOT a leap year!")


if __name__ == '__main__':
    try:
        user_input = int(input('Enter'))
    except ValueError:
        print("ValueError")