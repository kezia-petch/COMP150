def capitalise_words(file_name, destination):
    """
    >>> capitalise_words("russia.txt", "russia_capitalised.txt")
    >>> f1 = open("russia_capitalised.txt")
    >>> text1 = f1.read()
    >>> f2 = open("russia_answer_capitalised.txt")
    >>> text2 = f2.read()
    >>> text1 == text2
    True
    >>> capitalise_words("antigua.txt", "antigua_capitalised.txt")
    >>> f1 = open("antigua_capitalised.txt")
    >>> text1 = f1.read()
    >>> f2 = open("antigua_answer_capitalised.txt")
    >>> text2 = f2.read()
    >>> text1 == text2
    True
    """
    file_in = open(file_name)
    file_out = open(destination, "w")
    text = file_in.read()
    word = text.split()
    for word in word:
        file_out.write(word.capitalize() + " ")
    file_in.close()
    file_out.close()
    
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
    
