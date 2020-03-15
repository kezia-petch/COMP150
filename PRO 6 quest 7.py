myfile = open("text.txt", "w")
myfile.write("I have a bunch\nof red roses")
myfile.close()
myfile = open('text.txt', 'r')
text = myfile.read()

def line_length(filename, line):
    file = open(filename)
    text = file.read().replace("\n","")
    i = 0
    new = ''
    while i < len(text):
        if text[i].isspace():
            new += '_'
        if i % line == 0 and i != 0:
            new += '\n' + text[i]
        else: new += text[i]
        i += 1
    return new

print(line_length("text.txt", 7))