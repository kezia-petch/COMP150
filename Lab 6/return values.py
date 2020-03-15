def area_of_circle(radius):
    if radius < 0:
        print("Warning: radius must be positive")
        return
    
    area = 3.14159 * radius**2

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def is_divisible(x, y):
    return x%y == 0

print(is_divisible(10, 2))

