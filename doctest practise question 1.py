def is_dope(number):
    """
    >>> is_dope(123)
    True
    >>> is_dope(321)
    True
    >>> is_dope(22)
    True
    >>> is_dope(232)
    False
    >>> is_dope(10)
    False
    """
    numbers = str(number)
    product = 1
    sum = 0
    for char in numbers:
        product = product * int(char)
        sum = sum + int(char)
    if product==sum:
        return True
    else: return False

    
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)

