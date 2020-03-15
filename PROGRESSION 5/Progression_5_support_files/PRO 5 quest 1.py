def letter_count(file_name):
    """
    >>> letter_count("russia.txt")
    3111
    >>> letter_count("antigua.txt")
    2974
    """
    file = open(file_name)
    text = file.read()
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
        else: count += 0
    return count

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)