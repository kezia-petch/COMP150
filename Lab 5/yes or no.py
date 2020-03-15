def yes_no():
    x = input("Yes or no? ")
    if x == "Y":
        print("You choose yes")
    elif x == "y":
        print("You choose yes")
    elif x == "Yes":
        print("You choose yes")
    elif x == "yes":
        print("You choose yes")
    elif x == "YES":
        print("You choose yes")
    else: print("You choose no")
    
yes_no()