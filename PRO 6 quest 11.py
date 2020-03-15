myfile = open("text.txt", "w")
myfile.write("I have a bunch\nof red roses")
myfile.close()
myfile = open('text.txt', 'r')
text = myfile.read()

def print_first_word(filename):
    file = open(filename)
    text = file.readline()
 #   words = text.split('\n')
 
 
    while text:
        s = text.split()
        i = 0
        while i < len(s):
            if i == 0:
                print(s[i], end = '')
            else:
                print('w' + ' ', end = '')
            i += 1
        print()
        text = file.readline()
 
 
 
 
 
 
 
 
 
 
 
 i = 0
    new = ""
    while i < len(words):
        new += words[i].split()[0]
        for words[i].split()!= [0]
            new += 'w' + ' '
        i += 1
    return new 

print(print_first_word("text.txt"))