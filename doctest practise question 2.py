def convert_phone(number):
    """
    >>> convert_phone(22)
    'cc'
    >>> convert_phone(1403)
    'bead'
    >>> convert_phone(345901)
    'defjab'
    """
    numberS = str(number)
    news=""
    for char in numberS:
        if char == '0':
            news += 'a'
        elif char == '1':
            news += 'b'
        elif char == '2':
            news += 'c'
        elif char == '3':
            news += 'd'
        elif char == '4':
            news += 'e'
        elif char == '5':
            news += 'f'
        elif char == '6':
            news += 'g'
        elif char == '7':
            news += 'h'
        elif char == '8':
            news += 'i'
        elif char == '9':
            news += 'j'
    return news 

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)