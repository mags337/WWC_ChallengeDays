'Create a program to calculate the area of a circle given its radius.'

import numpy as np

def circle_area(radius):
    if radius is None:
        return 'No input provided'
    try:
        radius = float(radius)
    except ValueError:
        return 'Invalid input. Please enter a numeric value'
    
    return np.pi * radius**2

def get_user_input():
    try:
        return float(input('Enter the radius: '))
    except ValueError:
        return None

if __name__ == '__main__':
    user_radius = get_user_input()

    if user_radius is not None:
        result = circle_area(user_radius)
        print(f'The area of a circle given a radius of {user_radius} cm is {result:.2f} cm2')
    else:
        print('Invalid input. Please enter a numeric value')
