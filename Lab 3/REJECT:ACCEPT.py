def signature():
    print("Yours Sincerely")
    print("Humphrey Hopalong")

def reject(name):
    print("Dear", name)
    print("I am sorry to inform you that you do not have the job")
    signature()
    
def accept(name):
    print("Dear", name)
    print("I am pleased to inform you that you have the job")
    signature()
    
reject("Bill")
print()
reject("Amanda")
print()
accept("Vicki")
    