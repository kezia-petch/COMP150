def new_line ():
    print()
def three_lines ():
    new_line ()
    new_line ()
    new_line ()
# three_lines ().
print("First Line.")
print("Second Line.")
def nine_lines ():
    three_lines ()
    three_lines ()
    three_lines ()
print("First Line.")
nine_lines ()
print("Second Line.")
def clear_screen ():
    nine_lines ()
    nine_lines ()
    nine_lines ()
    nine_lines ()
    three_lines ()
    new_line ()
clear_screen ()

