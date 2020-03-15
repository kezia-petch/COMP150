def water_state():
    x = int(input("Temperature? "))
    if x > 100:
            print("Steam")
    elif x < 0:
            print("Ice")
    else: print("Liquid")

water_state()

