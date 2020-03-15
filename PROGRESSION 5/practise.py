def find_string(filename, destination, string, string2):
    file_in = open(filename)
    file_out = open(destination, 'w')
    text = file_in.read()
    words = text.split()
    for word in words:
        if string in word:
            file_out.write(word + " ")
    file_in.close()
    file_out.close()
    
