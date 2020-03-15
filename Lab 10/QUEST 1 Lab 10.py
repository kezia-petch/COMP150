def vowels_replaced(word):
    new_string = ""
    for char in word:
            if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == 'o' or char == "O" or char == "u" or char == "U" in word:
                new_string += "_"
            elif char == "\n":
                new_string += char
            else: new_string += char
    return new_string

myfile = open("newfile.txt", "w")
myfile.write("Hubble\nbubble\ntoil\nand\ntrouble")
myfile.close()

file = open("newfile.txt")
text = file.read()
words = text.split()
for word in words:
    print(vowels_replaced(word))




            