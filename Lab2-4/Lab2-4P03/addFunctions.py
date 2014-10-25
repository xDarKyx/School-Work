import time
''''List with the only valid types of expenses allowed for the dictionary'''
expTypes=["Transport","Food","House keeping","Clothing","Telephone&Internet","Others"]

'''add() function: adds to a specific day a specific type and a amount of expense'''
def add(expenses):
    t=input("Type:") #Type of exp
    d=input("Day:")# Day
    if(t in expTypes) and (int(d) in range(1,31)):
        td=t+d # Merge(combine) Type & Day
        v=int(input("Enter value:")) # Value
        expenses[td]=expenses.get(td)+v #Adds
        print("")
        print("Added",v,"RON for",t,"on day:",d)
    else:
        if(t in expTypes): #if the type is correct, prints out that the day is not valid and returns to add function
            print("")
            print("Please insert a day from range 1-31")
            add(expenses)
        else:
            print("")
            print("Invalid type, please enter a valid one.")
            add(expenses)
            
'''addToday() function: adds to the date of today new expense'''
def addToday(expenses):
    t=input("Type:") #Type of exp
    d=time.strftime("%d")# day number of today
    if(t in expTypes) and (int(d) in range(1,31)):
        td=t+d # Merge(combine) Type & Day
        v=int(input("Enter value:")) # Value
        expenses[td]=expenses.get(td)+v #Adds 
        print("")
        print("Added",v,"RON for",t,"on day:",d)
    else:
        if(t in expTypes): #if the type is correct, prints out that the day is not valid and returns to add function
            print("")
            print("Please insert a day from range 1-31")
            addToday(expenses)
        else:
            print("")
            print("Invalid type, please enter a valid one.")
            addToday(expenses)