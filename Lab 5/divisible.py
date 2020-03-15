def is_divisible_by_3(x):
    if x%3 == 0:
        print("This number is divisible by 3")
    else:
        print("This number is not divisible by 3")

def is_divisible_by_5(x):
    if x%5 == 0:
        print("This number is divisible by 5")
    else:
        print("This number is not divisible by 5")
        
def is_divisible(x,y):
    if x%y == 0:
        print(x, "is divisible by", y)
    else:
        print(x, "is not divisible by", y)
        
is_divisible(10, 2)
