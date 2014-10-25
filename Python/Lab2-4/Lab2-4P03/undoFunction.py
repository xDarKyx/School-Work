'''undoOp() function: restores the list from before the last operation'''
def undoOp(undoExp,expenses):
    if(undoExp==expenses):
        print("")
        print("No operations have been made that changed the list")
    else:
        for k in undoExp:
            expenses[k]=undoExp.get(k)
        print("")
        print("The last operation has been undone")
        print("")
        print("The Expenses before operation are back:")
        
        validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
        validDigits="123456789" # Valid digits for forming day
        print("")
        for k in expenses:
            t=''.join(c for c in k if c in validLetters) #gets type name
            d=''.join(c for c in k if c in validDigits) #gets day
            print("Day:",d,"Type:",t,"Price:",expenses.get(k))

'''This function updates the undoExp dictionary '''
def updateUndo(expenses,undoExp):
    for k in expenses:
        undoExp[k]=expenses.get(k)