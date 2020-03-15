myfile = open("text.txt", "w")
myfile.write("I have a bunch\nof red roses")
myfile.close()
myfile = open('text.txt', 'r')
text = myfile.read()

def print_first_word(filename):
    file = open(filename)
    text = file.read()
    words = text.split('\n')
    i = 0
    new = ""
    while i < len(words):
        print(words[i].split()[0])
        i += 1
    return new 

print(print_first_word("text.txt"))