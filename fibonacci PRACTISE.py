def fibonacci(x):
    new = ''
    i = 0
    n1 = 1
    n2 = 1
    nn = 0
    NN = 0
    while nn < x:
        nn = n1 + n2
        if nn > x:
            return NN
        else:
            NN = nn
            n1 = n2
            n2 = nn
        i += 1
    return NN

print(fibonacci(143))

