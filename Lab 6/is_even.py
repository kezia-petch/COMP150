def is_even(n):
    if n%2 == 0:
        return True
    else: return False

print(is_even (2))

def is_odd(n):
    return n%2 != 0
    
print(is_odd(1))

def is_factor(x, y):
    if y%x == 0:
        return True
    else: return False
    
print(is_factor(3,12))
