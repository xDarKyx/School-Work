''''List with the only valid types of expenses allowed for the dictionary'''
expTypes=["Transport","Food","House keeping","Clothing","Telephone&Internet","Others"]

'''display() function: displays a specific expense type from a specific day '''
def display(expenses):
    t=input("Type:")
    d=input("Day:")
    td=t+d # Combine Type & Day
    if(t in expTypes) and (int(d) in range(0,32)):
        print("")
        print("In Day:",d,"are spent",expenses.get(td),"RON for",t)
    else:
        if(t in expTypes): #if the type is correct, prints out that the day is not valid and returns to add function
            print("")
            print("Please insert a day from range 1-31")
            display(expenses)
        else:
            print("")
            print("Invalid type, please enter a valid one.")
            display(expenses)
    
'''displayAll() function: displays all expenses from all days'''
def displayAll(expenses):
    validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
    validDigits="123456789" # Valid digits for forming day
    print("")
    for k in expenses:
        t=''.join(c for c in k if c in validLetters) #gets type name
        d=''.join(c for c in k if c in validDigits) #gets day
        print("---------------------")
        print("Day",d,"Type:",t,"Price:",expenses.get(k))

'''Displays all the expenses greater than a given number'''
def displayGreater(expenses):
    n=int(input("Enter the value :"))
    validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
    validDigits="123456789" # Valid digits for forming day
    print("")
    for k in expenses:
        if(expenses[k]>n):
            t=''.join(c for c in k if c in validLetters) #gets type name
            d=''.join(c for c in k if c in validDigits) #gets day
            print("---------------------")
            print("Day",d,"Type:",t,"Price:",expenses.get(k))
            
'''displaySD function: displays all the expenses from the first to the specified day smaller than a given number'''            
def displaySD(expenses):
    n=int(input("Enter the maximum value :")) # Maximum value to display
    m=int(input("Enter the last day:")) # Last day to display
    validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
    validDigits="123456789" # Valid digits for forming day
    print("")
    for k in expenses:
        t=''.join(c for c in k if c in validLetters) #gets type name
        d=''.join(c for c in k if c in validDigits) #gets day
        if(expenses[k]<=n) and (int(d)<=m): # Verifies if the expenses value and days are smaller
            print("---------------------")
            print("Day",d,"Type:",t,"Price:",expenses.get(k)) # Displays them
            