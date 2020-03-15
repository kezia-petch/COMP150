myfile = open("text.txt", "w")
myfile.write("123,15,2017\n4264,25,2003\n2014,22,1998\n4721,16,2017")
myfile.close()
myfile = open('text.txt', 'r')
text = myfile.read()

def id_format(filename):
    file = open(filename)
    text = file.read().replace(",", " ")
    i = 0
    new = ""
    print("ID age year")
    while i < len(text):
        new += text[i]
        i += 1
    return new

print(id_format('text.txt'))
        

