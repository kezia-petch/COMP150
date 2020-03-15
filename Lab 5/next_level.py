def next_level(a, b, c, d, e, f):
    if (a + b + c + d + e + f) - min(a, b, c, d, e, f) == 200:
        print("Pass")
    else: print("Repeat")
    
next_level(1, 2, 3, 4, 5, 6)