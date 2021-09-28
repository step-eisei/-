b=50
for t in range (100):
    print("are you older than "+str(b)+"?")
    a=input("input yes or no:",) 
    if a=="yes":
        for i in range (1,10):
            c=input("are you older than "+str(d)+"? input yes or no:",)
            d=50+b/2
            if c=="yes":
                print("you are "+str(d)+"!")
            else:
                None
    elif a=="no":
        for i in range (1,10):
            e=input("are you older than "+str(d)+"? input yes or no:",)
            d=50-b/2
            if e=="yes":
                print("you are "+str(d)+"!")
            else:
                None
