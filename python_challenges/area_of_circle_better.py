'Create a program to calculate the area of a circle given its radius.'

'The calculates the area of a circle given its radius, based on the user input given'

import numpy as np

def circle_area(radius):
    if radius is None:
        return 'No input provided'
    try:
        radius = float(radius)
    except ValueError:
        return print('----Invalid input. Please enter a numeric value----')
    
    return np.pi * radius**2

def get_user_input():
    try:
        return float(input('Enter the radius: '))
    except ValueError:
        print ('----Invalid input. Please enter a numeric value----')
        return None

if __name__ == '__main__':
    user_radius = get_user_input()
    result = circle_area(user_radius)
    print(f'The area of a circle given a radius of {user_radius} cm is {result:.2f} cm2')
