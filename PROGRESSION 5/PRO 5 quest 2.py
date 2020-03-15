def count_possible_sentences(file_name):
    """
    >>> count_possible_sentences("russia.txt")
    22
    >>> count_possible_sentences("antigua.txt")
    27
    >>> count_possible_sentences("test.txt")
    1
    """
    file_in = open(file_name)
    text = file_in.read()
    
    words = text.split()
    count = 0
    for word in words:
        if word[-1] in "!?.":
            count+=1
    file_in.close()          
            
    return count

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)