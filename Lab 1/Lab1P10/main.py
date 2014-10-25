####Greatest Number 'Created by Feher-Simon Sandor 10.04.2014'####

n=int(input("Dati n="))
list1=[]
i=0
while(n>=1):
    list1.insert(i, n%10)
    n=n//10
    i=i+1
p=sorted(list1,reverse=True)
list2=map(str,p)
list2=''.join(list2)
list2=int(list2)
m=list2
print(m)