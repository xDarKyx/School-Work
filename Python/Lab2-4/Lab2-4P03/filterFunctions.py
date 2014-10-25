''''List with the only valid types of expenses allowed for the dictionary'''
expTypes=["Transport","Food","House keeping","Clothing","Telephone&Internet","Others"]

'''filterType() function: retains only a specific type of expense and removes the rest'''
def filterType(expenses):
    n=input("Type:")
    if(n in expTypes):
        validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
        for k in sorted(list(expenses)):
            t=''.join(c for c in k if c in validLetters) #gets day
            if(t==n): #Removes all types different from the entered type from the Dictionary
                ''''print(k,"is good")'''
            else:
                expenses.pop(k)
    else:
        print("")
        print("Invalid type, please enter a valid one.")
        filterType(expenses)
'''filterType() function: retains only a specific type of expense and removes the rest'''       
def filterTypePrice(expenses):
    n=input("Type:")
    if(n in expTypes):
        v=int(input("Price:"))
        validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
        for k in sorted(list(expenses)):
            t=''.join(c for c in k if c in validLetters) #gets day
            if(t==n) and (expenses.get(k)>=v): #Removes all types different from the entered type from the Dictionary
                ''''print(k,"is good")'''
            else:
                expenses.pop(k)
    else:
        print("")
        print("Invalid type, please enter a valid one.")
        filterTypePrice(expenses)