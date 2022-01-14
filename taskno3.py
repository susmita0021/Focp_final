import random 

def email_checker(email):
    """To check the given email is in correct format or not."""
    if email.count("@")!=1:
        return False
    
    if len(email.split("@")[0])<2:
        return False

    if email.split("@")[1]!="pop.ac.uk":
        return False
    
    return True

def ending(name):
    """To greet the user by displaying their name."""
    print(f"Thanks, {name}, for using PopChat. See you again soon!")
    
connection_error=[0,0,0,0,0,0,0,0,0,1]
operator_name=random.choice(["Synthia", "Jane", "Kim", "Kanya", "Ruby", "Phoebe"])#shows the operator in random format.
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
email=input("Please enter your Poppleton email address: ")

if email_checker(email):#checks whether the email is valid or not
    name = email.split("@")[0].capitalize()
    print(f"Hi, {name}! Thank you, and Welcome to PopChat! \n Hello!!{name}, I am {operator_name}.How can I help you.")

    while True:
        if random.choice(connection_error) == 1:
            print("NETWORK ERROR!!")
            ending(name)
            break
        question=input("Ask us your query or else write exit to exit!!\t")
        if any(char in question.lower() for char in ["bye","exit","help","goodbye","end"]):#if we use this words in the statement the progrma will close
            ending(name)
            break    
        elif("wifi" in question.lower()):
            print("WiFi is fine here do check your device.")
        elif("library" in question.lower()):
            print("The library is closed today.")
        elif "deadline" in question.lower():
            print( "Your deadline has been extended by two working days.")
        elif "book" in question.lower():
            print( "You can access the book from the library")
        elif "cafe" in question.lower():
            print( "The cafe is right next to the library")
        elif "classes" in question.lower():
            print( "You have no classes today")
        elif "result"in question.lower():
            print("You should go to college portal for result.But will be out within this week!!")
        else:
            print(random.choice(["I didn't understand","match not found","I see","sorry", "Oh, yes, I see.", "Is it?"]))#if the statement is out of the given words it will show these statement 
            
else:
    print("This email is not valid")#it checks wheather email is in asked format or not if not give the output as invalid.
    email_checker(email)#function call