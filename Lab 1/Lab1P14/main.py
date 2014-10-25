####Perfect Number 'Created by Feher-Simon Sandor 10.04.2014'####


def perfect(n): #Functia perfect
    i=0
    d=1
    list=[]
    
    while(d<=n/2):
        if(n%d == 0):
            list.insert(i, d) # Adauga divizorii lui n in lista
        d=d+1
    suma=sum(list) # Suma divizorilor
    if (suma==n): # Verifica daca n este numar perfect
        return 1
    else:
        return 0
    
def main():
    n=int(input("Dati n="))
    m=n # Memoram numarul citit de la tastatura
    if(n<2): #Verifica n
        print("Introduceti un numar natural mai mare decat 1")
        main()
    else:
        while(perfect(n)==0):
            n=n+1
            perfect(n)
        else:
            print(n," este cel mai mic numar perfect , mai mare decat",m)

main()