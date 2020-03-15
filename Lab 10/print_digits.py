def print_digits(n):
    """
    >>> print_digits(13789)
    9 8 7 3 1
    >>> print_digits(39874613)
    3 1 6 4 7 8 9 3
    >>> print_digits(213141)
    1 4 1 3 1 2
    """
    string = str(n)
    text = string.split()
    new_text = ""
    for word in text:
        new_text += word[:len(word)] + word[:len(word)-1] + word[:len(word)-2] + word[:len(word)-3] + word[:len(word)-4] + word[:len(word)-5] + word[:len(word)-6] + word[:len(word)-7]
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)