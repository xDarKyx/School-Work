####Prime Number 'Created by Feher-Simon Sandor 10.04.2014'####
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
def main():
    n=int(input("Dati n="))
    m=n
    if(n<3):
        print("Dati un numar natural mai mare decat 2")
        main()
    else:  
        while(prime(n)==0):
            n=n-1
            prime(n)
        else:
            print(n,"este cel mai mare numar prim , mai mic decat",m)
main()