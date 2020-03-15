def dollars(filename):
    file = open(filename)
    text = file.read()
    words = text.split()
    new_string = ""
    for word in words:
        for char in word:
            if char == "K":
                new_string += "$" + word + ",000" + "\n"
    return new_string

my_file = open('numbers.txt', 'w')
my_file.write(str("35K 15K 353K 1K 30K 54K 44K 501K"))
my_file.close()

print(dollars('numbers.txt'))