myfile = open("text.txt", "w")
myfile.write("I have a bunch\nof red roses")
myfile.close()
myfile = open('text.txt', 'r')
text = myfile.read()

def line_length(filename, number):
    file = open(filename)
    text = file.read()
    word = text.split()
    i = 0
    new = ''
    while i < len(word):
        if i % number == 0 and i != 0:
            new += word[i]
        i += 1
    return new

print(line_length("text.txt", 3))