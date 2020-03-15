def function_a ():
    print("function_a was called")

def function_b ():
    print("function_b was called")
    
def function_c ():
    print("function_c was called")
    
def dispatch():
    x = input("What function would you like? ")
    if x == "a":
        function_a ()
    elif x == "b":
        function_b ()
    elif x == "c":
        function_c ()
    else:
        print("Invalid choice.")


dispatch()