def dollars(filename):
    file = open(filename)
    text = file.read()
    words = text.split()
    new_string = ""
    for word in words:
        new_string += "$" + word + ",000" + "\n"
    return new_string

my_file = open('numbers.txt', 'w')
my_file.write("35 15 353 1 30 54 44 501")
my_file.close()

print(dollars('numbers.txt'))
        