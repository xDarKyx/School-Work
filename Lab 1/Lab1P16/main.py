####Perfect Number 'Created by Feher-Simon Sandor 10.04.2014'####


def perfect(n): #Functia perfect verifica daca numarul este perfect
    i=0 #contor pentru valoarea pozitiei elementului
    d=1 #contor pentru valoarea elementului
    list=[] #empty list
    
    while(d<=n/2): # Adauga divizorii lui n in lista
        if(n%d == 0):
            list.insert(i, d) 
        d=d+1
    suma=sum(list) # Suma divizorilor
    if (suma==n): # Aici se verifica daca n este numar perfect
        return 1
    else:
        return 0
    
def main():
    n=int(input("Dati n=")) #Se citeste o valoare de la tastatura
    m=n # Memoram numarul citit de la tastatura
    if(n<2): #Verifica daca n este mai mare decat 2
        print("Introduceti un numar natural mai mare decat 1")
        main()
    else: #Daca Perfect(n) este fals ,repeta functia n pana se va gasi un numar perfect
        while(perfect(n)==0):
            n=n-1 # Numarul mai mic cu 1 decat cel dat
            perfect(n) #Apeleaza functia Perfect(n)
        else: #Altfel returneaza n
            print(n," este cel mai mare numar perfect , mai mic decat",m)

main()