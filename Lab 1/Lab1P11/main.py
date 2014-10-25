#Starts n
n=int(input("Dati n="))

list1=[]
i=0
while(n>=1):
    list1.insert(i,n%10)
    n=n//10
    i=i+1
list1=sorted(list1)
print(list1)

#Starts m
m=int(input("Dati m="))

list2=[]
j=0
while(m>=1):
    list2.insert(j,m%10)
    m=m//10
    j=j+1
list2=sorted(list2) #Sorts list2
print(list2)

list1=list(set(list1)) #Removes duplicated elements from list1
list2=list(set(list2)) #Removes duplicated elements from list2

if(list1==list2):
    print("The numbers have the same digits!! =D")
else:
    print("The numbers don't have the same digits! =(")