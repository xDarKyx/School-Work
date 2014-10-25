'''Created by Feher-Simon Sandor 10.20.2014'''
import os
clear = lambda: os.system('cls') # For clearing the Console

'''Importing functions from files'''
from addFunctions import *
from modifyFunctions import *
from characteristicFunctions import *
from displayFunctions import *
from filterFunctions import *
from undoFunction import *
from generateList import *



'''Loading from memory some elements to list(in pairs)'''
pairs = [("Transport1", 33), ("Transport2", 35), ("Food1", 33) ,("Food2",35), ("House Keeping1", 33) ,("House Keeping2",31), ("Clothing1", 33) ,("Clothing2",35), ("Telephone&Internet1", 33) ,("Telephone&Internet2",35), ("Others1", 33) ,("Others2",35)] # We load from memory
generate(pairs) #Only to generate rest of days with value 0'''

'''Converting the list to dictionary'''
expenses=dict(pairs) # Convert to dictionary
'''Backup dictionary for our initial dictionary'''
undoExp=dict(pairs)  
''''List with the only valid types of expenses allowed for the dictionary'''
expTypes=["Transport","Food","House keeping","Clothing","Telephone&Internet","Others"]

def printAvailableTypes():
    print("")
    print("The following types are available:")
    for k in expTypes:
        print("- ",k)
    print("!!NOTE:You have to write them exactly as displayed!!")
    print("")

'''Graphical Menu Interface of the Program'''
def main():
    
    k=1
    while k in range(1,4):
        print("")
        print(" #### MENU ####")
        print(" 1.Add")
        print(" 2.Modify")
        print(" 3.Display")
        print(" 4.Characteristicts")
        print(" 5.Filter")
        print(" 6.Undo last operation")
        print(" 0.Exit")
        k=int(input("Choose path:"))
        clear() #Clear console
        if k==1:
            print("")
            print(" 1.Add expenses for a certain day")
            print(" 2.Add expenses for today")
            cmd=int(input("Choose path:"))
            clear() #Clear console
            if (cmd==1):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                add(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif (cmd==2):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                addToday(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
        elif k==2:
            print("")
            print(" 1.Delete specific expenese from  specific day")
            print(" 2.Delete all expenses from specific type")
            print(" 3.Replace specific expense")
            print(" 4.Delete specific day expenses")
            print(" 5.Remove all expenses between two spc. days")
            cmd=int(input("Choose path:"))
            clear() #Clear console
            if (cmd==1):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                remove(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif (cmd==2):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                removeType(expenses)
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif (cmd==3):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                replace(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif (cmd==4):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                removeDay(expenses)
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif (cmd==5):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                rangeRemove(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
        elif k==3:
            print("")
            print(" 1.Display specific expenese from  specific day")
            print(" 2.Display all expenses from month")
            print(" 3.Display all expenses greater than a given number")
            print(" 4.Display all expenses smaller than a given number until a given day")
            cmd=int(input("Choose path:"))
            clear() #Clear console
            if(cmd==1):
                printAvailableTypes()
                display(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif(cmd==2):
                displayAll(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif(cmd==3):
                displayGreater(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
            elif(cmd==4):
                displaySD(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
        elif k==4:
            print("")
            print(" 1.Sum of a specific type of expense")
            print(" 2.Max Day Sum")
            print(" 3.Day in which was spent exactly n-RON for each category")
            print(" 4.Sort the total daily expenses in ascending order")
            print(" 5.Sort the total type expenses in descending order")
            cmd=int(input("Choose path:"))
            clear() #Clear console
            if (cmd==1):
                printAvailableTypes()
                sumType(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
            elif (cmd==2):
                maxDay(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
            elif (cmd==3):
                exactN(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
            elif (cmd==4):
                ascSortDay(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
            elif (cmd==5):
                dscSortType(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
        elif k==5:
            print("")
            print(" 1.Filter by type")
            print(" 2.Filter by type and price higher than")
            cmd=int(input("Choose path:"))
            clear() #Clear console
            if (cmd==1):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                filterType(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
            elif (cmd==2):
                updateUndo(expenses,undoExp) #Updates the undoExp before executing changes to expenses dictionary
                printAvailableTypes()
                filterTypePrice(expenses)
                print("")
                input("Press enter to continue...") #Pause for results
                clear() #Clear console
                main()
        elif k==6:
            undoOp(undoExp,expenses)
            print("")
            input("Press enter to continue...") #Pause for results
            clear() #Clear console
            main()
            
def startApp():
    print("--------------------------------------------------------")
    print("           P3. Family expenses management")
    print("--------------------------------------------------------")
    print("         Credits: Feher-S. Sandor 10.20.2014")
    print("--------------------------------------------------------")
    
    main()
    
startApp()
    