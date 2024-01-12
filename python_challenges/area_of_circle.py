'Create a program to calculate the area of a circle given its radius.'

import numpy as np

input = input("Enter the radius: ")

def circle_area(radius):
        area = np.pi * radius**2
        print(f"The area of a circle given a radius of {radius} cm is {area:.2f} cm2")
        return area
try: 
    circle_area(float(input))
except:
    print("Circle radius must be a float or integer")