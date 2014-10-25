####Twin Number 'Created by Feher-Simon Sandor 10.04.2014'####
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

def start(n):
    i=0
    list1=[]
    while(len(list1)<2):
        if(prime(n)==1):
            list1.insert(i, n)
            i=i+1
        n=n+1
        prime(n)
    print(list1)
    
    n=list1[1]
    m=list1[0]
    if((n-m)==2):
        print(n,"-",m," = 2")
    else:
        n=n+1
        start(n)
        

        

def main():
    n=int(input("Dati n="))
    if(n<0):
        print("Dati un numar natural mai mare decat 0")
        main()
    else:  
        start(n)
    
main()