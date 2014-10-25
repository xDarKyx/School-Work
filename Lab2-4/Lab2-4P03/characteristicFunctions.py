import operator
''''List with the only valid types of expenses allowed for the dictionary'''
expTypes=["Transport","Food","House keeping","Clothing","Telephone&Internet","Others"]

'''sumType() function: returns the sum  of expenses from a specific type from the whole month'''
def sumType(expenses):
    t=input("Type:")
    if(t in expTypes):
        i=1 #Days start from 1
        total=0 # Total is our sum of our expense on the whole month
        c=0 #Contor
        while(c<31): #We start a loop that works until our i. is smaller than our list length.
            for k in sorted(list(expenses)): # We use sorted list(expenses) to force copy of expenses dictionary and we can update expenses dictionary
                d=str(i) #We convert integer i to string and memorize as d(For name search)
                if(k==t+d):
                    total=total+expenses.get(k)
                    i+=1
            c+=1
        print("")
        print("The sum of",t,"is:",total,"RON")
    else:
        print("")
        print("Invalid type, please enter a valid one.")
        sumType(expenses)

'''makeSumDay() function: is used to calculate each days total expenses and insert 
them into a list as pairs(day, total)'''
def makeSumDay(n,maxList,expenses):
    total=0 # Total is our sum of our expense on the whole month
    validDigits="123456789" # Valid digits for forming day
    for k in sorted(list(expenses)): # We use sorted list(expenses) to force copy of expenses dictionary and we can update expenses dictionary
        d=''.join(c for c in k if c in validDigits) #gets day
        if(d==n):
            total=total+expenses.get(k) #Calculates sum of day
    maxList.append((n,total))#Inserts into our maxList the day and total of day as pair
    
def makeSumType(n,maxList,expenses):
    total=0 # Total is our sum of our expense on the whole month
    validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
    validDigits="123456789" # Valid digits for forming day
    for k in sorted(list(expenses)): # We use sorted list(expenses) to force copy of expenses dictionary and we can update expenses dictionary
        d=''.join(c for c in k if c in validDigits) #gets day
        t=''.join(c for c in k if c in validLetters) #gets type
        td=t+d
        if(td==n):
            total=total+expenses.get(k) #Calculates sum of day
    maxList.append((n,total))#Inserts into our maxList the day and total of day as pair
    
'''maxDay() function: displays the day with the biggest expenses of the month '''
def maxDay(expenses):
    maxList=[]
    validDigits="123456789" # Valid digits for forming day
    for k in expenses:
        d=''.join(c for c in k if c in validDigits) #gets day
        makeSumDay(d,maxList,expenses) #Calling function makeSumDay
    totalDay=dict(maxList) #Creating a new dictionary with the values of maxList
    maxExpDay=max(totalDay,key=totalDay.get) #Getting the day number with highest value
    print("")
    print ("The day with maximum expenses is day: ",maxExpDay,"with a price of:",totalDay.get(maxExpDay),"RON")

'''exactN() function: displays the day which in were spent exactly n-RON for each type(category)'''
def exactN(expenses):
    n=int(input("Enter the value:"))
    validDigits="123456789" # Valid digits for forming day
    nPriceExpenses={} #This dictionary will contain type and day with price n
    for k in expenses:
        if(expenses.get(k)==n):
            nPriceExpenses[k]=expenses.get(k) #Introduce into our nPriceExpenses dict the key(day) and value(price)
    exactDays={}
    for k in nPriceExpenses:
        d=''.join(c for c in k if c in validDigits) #gets day
        #Checks if all types are in nPriceExpenses
        if("Telephone&Internet"+d in nPriceExpenses) and ("House Keeping"+d in nPriceExpenses) and("Transport"+d in nPriceExpenses) and ("Clothing"+d in nPriceExpenses) and ("Others"+d in nPriceExpenses):
            #print("In Day:",d,"has been spent",n,"RON for all types")
            exactDays[d]=n
    check=0  #        
    for k in exactDays:
        if(exactDays.get(k)==n):
            print("")
            print("In day:",k,"has been spent exactly",n,"RON")
            check=1
    if(check==0):
        print("")
        print("Couln't find any day.")
            
'''ascSortDay() function: sorts ascending the total price of each day(uses makeSumDay() function for doing the sums) '''
def ascSortDay(expenses):
    maxList=[]
    validDigits="123456789" # Valid digits for forming day
    for k in expenses:
        d=''.join(c for c in k if c in validDigits) #gets day
        makeSumDay(d,maxList,expenses) #Calling function makeSumDay
    totalDay=dict(maxList) #Creating a new dictionary with the values of maxList
    print("")
    print("Sorted expenses ascending")
    #Sorting ascending the dictionary
    sortedExp=sorted(totalDay.items(),key=operator.itemgetter(1))
    print("-Day-Price-")
    for k in sortedExp:
        print(k)


'''dscSortType(): Displays the type total expenses of the month(the sum of each type) sorted descending'''
def dscSortType(expenses):
    maxList=[]
    validDigits="123456789"
    validLetters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST &" # Valid letters for forming Type
    for k in expenses:
        t=''.join(c for c in k if c in validLetters) #gets day
        d=''.join(c for c in k if c in validDigits) #gets day
        td=t+d
        makeSumType(td,maxList,expenses) #Calling function makeSumDay
    totalDay=dict(maxList) #Creating a new dictionary with the values of maxList
    print("")
    print("Sorted expenses descending:")
    newExp=[]
    #sortedExp=sorted(totalDay.items(),key=operator.itemgetter(1),reverse=True)
    for k in totalDay:
        t=''.join(c for c in k if c in validLetters) #gets day
        d=''.join(c for c in k if c in validDigits) #gets day
        newExp.append((d,t,totalDay.get(k)))
    
    print("")
    print("-Day-Type-Total-")
    for k in sorted(newExp, key=operator.itemgetter(2),reverse=True):
        print(k)
