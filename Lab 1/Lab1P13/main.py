n=int(input("Dati n="))

def prime(n):
    i=2
    check=0
    while(i<=n/2) :
        if (n%i==0):
            print("Este divizibil cu",i);
            check=1
        else:
            print("Nu este divizibil cu",i)
            
        i=i+1
    if(check==1):
        return 0
       # print("Number is not prime")
    else:
        return 1
       # print("Number is prime")
       
def sequence(n):
    list=[]
    i=1
    d=0
    q=1
    while(i<=n):
        list.insert(d, i)
        d=d+1
        i=i+1
    while(q<n):
        if(prime(list[q])==0):
            print(list[q])
        q=q+1
    print(list)
        
sequence(n)