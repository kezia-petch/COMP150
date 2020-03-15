myfile = open("roses2.txt", "w")
myfile.write("I have a big bunch of red roses, there are 12, they are great")
myfile.close()

myfile = open("roses2.txt", 'r')
text = myfile.read()
print(text)

myfile2 = open("roses3.txt", "w")
myfile2.write("they are nice")