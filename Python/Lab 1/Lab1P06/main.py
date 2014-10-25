n=int(input("Dati n="))

list1=[0,1,1,2]
p=len(list1)+1
while(n>len(list1)):
    list1.insert(p,list1[len(list1)-1]+list1[len(list1)-2])
    p=p+1

print(list1)

m=list1[len(list1)-1]+list1[len(list1)-2]
print("The answer is:",m)