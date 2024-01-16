'Create a program to calculate the area of a circle given its radius.'

'The calculates the area of a circle given its radius, based on the user input given'

import numpy as np

user_input = input("Enter the radius: ")

def circle_area(radius):
        area = np.pi * radius**2
        print(f"The area of a circle given a radius of {radius} cm is {area:.2f} cm2")
        return area
try: 
    circle_area(float(user_input))
except:
    print("Circle radius must be a float or integer")