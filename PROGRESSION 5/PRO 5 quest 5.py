def save_word_lengths(file_name, destination):
    """
    >>> save_word_lengths("russia.txt", "russia_word_lengths.txt")
    >>> f1 = open("russia_word_lengths.txt")
    >>> text1 = f1.read()
    >>> f2 = open("russia_answer_word_lengths.txt")
    >>> text2 = f2.read()
    >>> text1 == text2
    True
    >>> save_word_lengths("antigua.txt", "antigua_word_lengths.txt")
    >>> f1 = open("antigua_word_lengths.txt")
    >>> text1 = f1.read()
    >>> f2 = open("antigua_answer_word_lengths.txt")
    >>> text2 = f2.read()
    >>> text1 == text2
    True
    """
    file_in = open(file_name)
    file_out = open(destination, 'w')
    text = file_in.read()
    word = text.split()
    for word in word:
        file_out.write(str(len(word)) + " ")
        
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
        
