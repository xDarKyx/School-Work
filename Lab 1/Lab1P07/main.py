####Proper Factors 'Created by Feher-Simon Sandor 10.04.2014'####
n=int(input("Dati n="))
list1=[]
i=0
d=1
while(d<=n/2):
    if(n%d==0):
        list1.insert(i, d)
        i=i+1
    d=d+1
print("Divizorii sunt :",list1)

j=0
q=1
while(j<len(list1)):
    q=q*list1[j]
    j=j+1
print(q)