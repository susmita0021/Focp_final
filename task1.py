print("Stop! Who would cross the Bridge of Death\n Must answer me these questions three, 'ere the other side he see.'")
name=input("What is your name?")#to input the name from user.
if name.lower()=="arthur":
    print("My liege! You may pass!")
else:
    seek=input("What do you seek?")
    if "grail" in seek:#if condition with in operator cheks if input has grail in it.
        print("ok! now the last question")
        color=input("What is your favourite color?")
        if name[0].upper() in color[0].upper():#it checks the first letters of color and name are same or not.
            print("You may pass")
        else:
            print("You may not pass!!")
    else:
        print("You may not pass!")
            
        
        
