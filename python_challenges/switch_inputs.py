'Create a program that swaps the values of two variables.'

x = input("input one")
y = input("input two")

def swap_values(x, y):
    print(f'input x, y = {x, y}')
    x, y = y, x
    print(f'output x, y= {x, y}')
    return x, y

print(swap_values(x,y))

