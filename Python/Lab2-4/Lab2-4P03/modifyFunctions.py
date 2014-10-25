''''List with the only valid types of expenses allowed for the dictionary'''
expTypes=["Transport","Food","House keeping","Clothing","Telephone&Internet","Others"]
    
'''remove() function : removes from a specific day a specific type of expense'''    
def remove(expenses):
    t=input("Type:")
    d=input("Day:")
    td=t+d
    if(t in expTypes) and (int(d) in range(0,32)):
        expenses.pop(td)
        print("Expense removed succesfully!")
    else:
        if(t in expTypes): #if the type is correct, prints out that the day is not valid and returns to add function
            print("Day:",d,",is not a valid day")
            print("Please insert a day from range 1-31")
            remove(expenses)
        else:
            print("Type:",t,",does not exist")
            print("Please insert one of the following types")
            print(expTypes)
            remove(expenses)
    
'''removeDay() function: removes all expenses from a specific day'''

def removeDay(expenses):
    dr=input("Day to remove:") # Day to remove input
    if(int(dr) in range(0,32)):
        validDigits="123456789" # Valid digits for forming day
        i=0 #Contor
        while(i<len(list(expenses))): #We start a loop that works until our i. is smaller than our list length.
            for k in list(expenses):
                d=''.join(c for c in k if c in validDigits) #gets day
                if(dr==d):
                    expenses.pop(k)
                    print("Succesfully removed day expenses!")
            i+=1 # i gets bigger
    else:
        print("Please enter a day in range 1-31")
        removeDay(expenses)

'''removeType() function: removes from the whole month a specific type of expense'''    
def removeType(expenses):
    t=input("Type:")
    if(t in expTypes):
        i=1 #Days start from 1
        c=0 #Contor
        while(c<31): #We start a loop that works until our i. is smaller than our list length.
            for k in sorted(list(expenses)): # We use sorted list(expenses) to force copy of expenses dictionary and we can update expenses dictionary
                d=str(i) #We convert integer i to string and memorize as d(For name search)
                if(k==t+d):
                    expenses.pop(k) # We remove the element if the element exists in the dictionary
                    print("The expense has been removed!")
                    i+=1
                    
            c+=1
    else:
        print("The type",t,"is not available")
        print("Only the following types are available")
        print(expTypes)
        removeType(expenses)
            
    
''' replace() function: replacing a cost from our expenses list if it exists'''
def replace(expenses):
    t=input("Type:") # Type
    d=input("Day:") # Day
    if(t in expTypes) and (int(d) in range(1,31)):
        v=input("New value:") # New value
        td=t+d # Our stored key
        if(td in expenses): # Checking if our value exists in our dictionary
            expenses[td]=v # Executing our update
            print("Succesfully edited value!") #Succcess
        else:
            print("The value does not exist!") # Sending our error ,we couldn't find the number
    else:
        if(t in expTypes): #if the type is correct, prints out that the day is not valid and returns to add function
            print("")
            print("Please insert a day from range 1-31")
            replace(expenses)
        else:
            print("")
            print("Invalid type, please enter a valid one.")
            replace(expenses)
        
'''rangeRemove() function: removes expenses between two given days(including those days)'''
def rangeRemove(expenses):
    d1=input("First day:") # First day of range
    d2=input("Last day:") #Last day of range
    if(int(d1) in range (1,31)) and (int(d2) in range (int(d1)+1,31)):
        validDigits="123456789" # Valid digits for forming day
        i=0 #Contor
        while(i<len(list(expenses))): #We start a loop that works until our i. is smaller than our list length.
            for k in list(expenses):
                d=''.join(c for c in k if c in validDigits) #gets day
                if(int(d) in range(int(d1)-1,int(d2)+1)): #Checks if the obtained numbers(days) are in the range of the given days
                    expenses.pop(k) #Removes them
                    print("Succesfully removed day expenses!")
            i+=1 # i gets bigger
    else:
        if(d1>d2):
            print("")
            print("First day has to be smaller than Last day.")
            rangeRemove(expenses)
        else:
            print("")
            print("Please insert days in range 1-31")
            rangeRemove(expenses)
    