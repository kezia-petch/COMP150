def word_longer_than(x):
    user_in = ""
    while len(user_in) < 12 or not user_in.isalpha():
        user_in = input("Please enter a word longer than " + str(x) + ": ")
        if len(user_in) < 12 or not user_in.isalpha():
            print("Try again")
    return user_in

print(word_longer_than(10))