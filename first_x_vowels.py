def first_x_vowels(filename, x):
    file_in = open(filename)
    text = file_in.read()
    i = 0
    result = ""
    while i < len(text) and len(result)<x:
        if text[i].lower() in "aeiou":
            result += text[i]
            i += 1
    file_in.close()
    return result

