def guess_right(x,y):
    if x == y:
        print("You win.", y, "is equal to", x)
    else:
        print("You lose.", y, "is not equal to", x)

def guessing():
    secret = 55
    guess = int(input("Guess a number between 50 and 100: "))
    guess_right(secret, guess)
    
guessing()