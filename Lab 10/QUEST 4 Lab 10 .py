def num_even_digits(n):
    """
    >>> num_even_digits(123456)
    3
    >>> num_even_digits(2468)
    4
    >>> num_even_digits(1357)
    0
    >>> num_even_digits(2)
    1
    >>> num_even_digits(20)
    2
    """
    String = str(n)
    count = 0
    for char in String:
        if int(char) % 2 == 0:
            count += 1
        else: count += 0
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)