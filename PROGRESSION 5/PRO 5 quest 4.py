def strip_punctuation(file_name, destination):
    """
    >>> strip_punctuation("russia.txt", "russia_no_punc.txt")
    >>> f1 = open("russia_no_punc.txt")
    >>> text1 = f1.read()
    >>> f2 = open("russia_answer_no_punc.txt")
    >>> text2 = f2.read()
    >>> text1 == text2
    True
    >>> strip_punctuation("antigua.txt", "antigua_no_punc.txt")
    >>> f1 = open("antigua_no_punc.txt")
    >>> text1 = f1.read()
    >>> f2 = open("antigua_answer_no_punc.txt")
    >>> text2 = f2.read()
    >>> text1 == text2
    True
    """
    file_in = open(file_name)
    file_out = open(destination, "w")
    text = file_in.read()
    for char in text:
        if char.isspace():
            file_out.write(" ")
        elif char.isalpha():
            file_out.write(char)
        elif char.isdigit():
            file_out.write(char)
        else: file_out.write("")
    file_in.close()
    file_out.close()
    
if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
